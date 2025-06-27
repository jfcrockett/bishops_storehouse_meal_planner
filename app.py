import streamlit as st
import random
import os
from typing import List, Dict
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def load_ingredients(filename: str = "ingredients.txt") -> Dict:
    """Load ingredient data from text file"""
    ingredients = {}
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                # Skip comments and empty lines
                if line.startswith('#') or not line:
                    continue
                
                # Parse line: ingredient_name | package_size | servings_per_package | unit
                parts = [part.strip() for part in line.split('|')]
                if len(parts) == 4:
                    name, size, servings, unit = parts
                    ingredients[name] = {
                        'size': float(size),
                        'servings': float(servings),
                        'unit': unit
                    }
    except FileNotFoundError:
        st.error(f"Could not find {filename}. Please make sure the file exists.")
        return {}
    
    return ingredients

def load_meals(filename: str = "meal_options.txt") -> Dict:
    """Load meal data from text file"""
    meals = {'Breakfast': {}, 'Lunch': {}, 'Dinner': {}}
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        current_meal_type = None
        current_meal_name = None
        current_ingredients = {}
        current_instructions = []
        reading_instructions = False
        
        for line in lines:
            line = line.strip()
            
            # Skip comments only
            if line.startswith('#'):
                continue
            
            # Handle empty lines (meal separators)
            if not line:
                # Empty line ends current meal
                if current_meal_name and current_meal_type:
                    meals[current_meal_type][current_meal_name] = {
                        'ingredients': current_ingredients.copy(),
                        'instructions': current_instructions.copy()
                    }
                # Reset for next meal
                current_meal_name = None
                current_ingredients = {}
                current_instructions = []
                reading_instructions = False
                continue
            
            # Check for meal type header
            if line.startswith('[') and line.endswith(']'):
                # Save previous meal if exists
                if current_meal_name and current_meal_type:
                    meals[current_meal_type][current_meal_name] = {
                        'ingredients': current_ingredients.copy(),
                        'instructions': current_instructions.copy()
                    }
                
                # Reset for new meal type
                meal_type = line[1:-1].title()
                current_meal_type = meal_type
                current_meal_name = None
                current_ingredients = {}
                current_instructions = []
                reading_instructions = False
                continue
            
            # Check for instructions header
            if line == "INSTRUCTIONS:":
                reading_instructions = True
                continue
            
            # If reading instructions
            if reading_instructions:
                # Remove number prefix if exists
                instruction = line
                if line[0].isdigit() and '. ' in line:
                    instruction = line.split('. ', 1)[1]
                current_instructions.append(instruction)
            
            # If not reading instructions, check for meal name or ingredient
            elif not reading_instructions:
                if '|' in line:
                    # This is an ingredient line
                    parts = [part.strip() for part in line.split('|')]
                    if len(parts) == 2:
                        ingredient, portion = parts
                        current_ingredients[ingredient] = float(portion)
                else:
                    # This is a meal name
                    # Save previous meal if exists
                    if current_meal_name and current_meal_type:
                        meals[current_meal_type][current_meal_name] = {
                            'ingredients': current_ingredients.copy(),
                            'instructions': current_instructions.copy()
                        }
                    
                    # Start new meal
                    current_meal_name = line
                    current_ingredients = {}
                    current_instructions = []
                    reading_instructions = False
        
        # Save the last meal
        if current_meal_name and current_meal_type:
            meals[current_meal_type][current_meal_name] = {
                'ingredients': current_ingredients.copy(),
                'instructions': current_instructions.copy()
            }
                
    except FileNotFoundError:
        st.error(f"Could not find {filename}. Please make sure the file exists.")
        return {}
    
    return meals

# Load data from files
MEAL_PORTIONS = load_ingredients()
MEALS = load_meals()

# Data is now loaded from external files above

def calculate_needed_quantity(ingredient: str, servings_needed: float, num_people: int) -> int:
    """Calculate how many packages/cans needed based on serving size and number of people"""
    if ingredient not in MEAL_PORTIONS:
        return max(1, round(servings_needed * num_people))
        
    item_info = MEAL_PORTIONS[ingredient]
    servings_per_package = item_info['servings']
    packages_needed = (servings_needed * num_people) / servings_per_package
    return max(1, round(packages_needed))

def convert_to_practical_measurement(ingredient: str, portion: float, num_people: int = 1) -> str:
    """Convert ingredient portions to practical measurements without requiring a scale"""
    if ingredient not in MEAL_PORTIONS:
        return f"{portion * num_people:.1f} portions"
    
    item_info = MEAL_PORTIONS[ingredient]
    total_amount = portion * item_info['size'] * num_people
    
    # Conversion mappings for common ingredients
    conversions = {
        'milk': {'ratio': 8, 'unit': 'cup(s)', 'name': 'milk'},  # 8 oz = 1 cup
        'butter': {'ratio': 16, 'unit': 'cup(s)', 'name': 'butter'},  # 16 oz = 1 cup (2 sticks)
        'honey': {'ratio': 12, 'unit': 'cup(s)', 'name': 'honey'},  # 12 oz ≈ 1 cup
        'mayo': {'ratio': 15, 'unit': 'cup(s)', 'name': 'mayo'},  # 15 oz ≈ 1 cup
        'ranch dressing': {'ratio': 16, 'unit': 'cup(s)', 'name': 'ranch dressing'},
        'peanut butter': {'ratio': 16, 'unit': 'cup(s)', 'name': 'peanut butter'},
        'raspberry jam': {'ratio': 20, 'unit': 'cup(s)', 'name': 'raspberry jam'},
        'salsa': {'ratio': 8, 'unit': 'cup(s)', 'name': 'salsa'},  # Easier to measure in cups
        'rolled oats': {'ratio': 3, 'unit': 'cup(s)', 'name': 'rolled oats'},  # 3 oz ≈ 1 cup
        'rice': {'ratio': 6, 'unit': 'cup(s)', 'name': 'uncooked rice'},  # 6 oz ≈ 1 cup
        'macaroni': {'ratio': 4, 'unit': 'cup(s)', 'name': 'uncooked macaroni'},  # 4 oz ≈ 1 cup
        'spaghetti': {'ratio': 4, 'unit': 'cup(s)', 'name': 'uncooked spaghetti'},  # 4 oz ≈ 1 cup
        'pancake mix': {'ratio': 4, 'unit': 'cup(s)', 'name': 'pancake mix'},  # 4 oz ≈ 1 cup
        'instant potatoes': {'ratio': 3, 'unit': 'cup(s)', 'name': 'instant potato flakes'},  # 3 oz ≈ 1 cup
        'cinnamon': {'ratio': 0.2, 'unit': 'teaspoon(s)', 'name': 'ground cinnamon'},  # 0.2 oz ≈ 1 tsp
    }
    
    # Special cases for count-based items
    if ingredient == 'eggs':
        count = portion * item_info['size'] * num_people
        return f"{int(round(count))} egg(s)"
    elif ingredient == 'bread':
        slices = portion * item_info['size'] * num_people
        return f"{int(round(slices))} slice(s) of bread"
    elif ingredient == 'tortillas':
        count = portion * item_info['size'] * num_people
        return f"{int(round(count))} tortilla(s)"
    elif ingredient == 'hot dog buns':
        count = portion * item_info['size'] * num_people
        return f"{int(round(count))} hot dog bun(s)"
    
    # Handle canned goods and pre-packaged items
    canned_items = [
        'fully cooked beef', 'beef stew', 'chili', 'pork and beans', 'tuna',
        'chicken breast pieces', 'chicken rotini soup', 'cream of chicken soup',
        'cream of mushroom soup', 'tomato soup', 'applesauce', 'peaches', 'pears',
        'corn', 'green beans', 'spaghetti sauce', 'diced tomatoes', 'black beans',
        'white beans', 'refried beans', 'honey nut o\'s', 'raisin bran',
        'macaroni and cheese', 'vanilla yogurt', 'cheddar cheese', 'raisins'
    ]
    
    if ingredient in canned_items:
        if total_amount < item_info['size']:
            # Less than a full package
            if total_amount < item_info['size'] * 0.25:
                return f"1/4 of a {item_info['size']} {item_info['unit']} {ingredient}"
            elif total_amount < item_info['size'] * 0.5:
                return f"1/3 of a {item_info['size']} {item_info['unit']} {ingredient}"
            elif total_amount < item_info['size'] * 0.75:
                return f"1/2 of a {item_info['size']} {item_info['unit']} {ingredient}"
            else:
                return f"3/4 of a {item_info['size']} {item_info['unit']} {ingredient}"
        else:
            # One or more full packages
            packages = total_amount / item_info['size']
            if packages <= 1.1:  # Close to 1 package
                return f"1 can/package of {ingredient} ({item_info['size']} {item_info['unit']})"
            else:
                return f"{packages:.1f} cans/packages of {ingredient} ({item_info['size']} {item_info['unit']} each)"
    
    # Use conversion table for measurable ingredients
    if ingredient in conversions:
        conv = conversions[ingredient]
        converted_amount = total_amount / conv['ratio']
        if converted_amount < 0.125:  # Less than 1/8
            # Convert to tablespoons
            tbsp = converted_amount * 16
            if tbsp < 0.5:
                tsp = tbsp * 3
                return f"{tsp:.0f} teaspoon(s) of {conv['name']}"
            else:
                return f"{tbsp:.1f} tablespoon(s) of {conv['name']}"
        else:
            return f"{converted_amount:.2f} {conv['unit']} of {conv['name']}"
    
    # Fallback for any remaining items
    return f"{total_amount:.1f} {item_info['unit']} of {ingredient}"

def calculate_ingredients(selected_meals: List[str], num_people: int, num_days: int) -> tuple[Dict[str, float], list]:
    """Calculate total ingredients needed for selected meals over the specified period."""
    import streamlit as st
    
    ingredients = {}
    meal_plan = []
    
    # Terminal debug output
    print("\n" + "="*60)
    print("🔍 DEBUG: Meal Planning Process")
    print("="*60)
    print(f"Selected meals: {selected_meals}")
    print(f"Number of people: {num_people}, Number of days: {num_days}")
    print()
    
    # Create meal plan
    for day_num in range(num_days):
        day_meals = {
            'Breakfast': [],
            'Lunch': [],
            'Dinner': []
        }
        for meal_type, meals in MEALS.items():
            available_meals = [m for m in selected_meals if m in meals]
            if available_meals:
                chosen_meal = random.choice(available_meals)
                day_meals[meal_type] = chosen_meal
                print(f"Day {day_num + 1} {meal_type}: {chosen_meal}")
        meal_plan.append(day_meals)
    
    print("\n🔍 DEBUG: Ingredient Calculation")
    print("-" * 40)
    
    # Calculate ingredients
    for day_num, day in enumerate(meal_plan):
        print(f"\nDay {day_num + 1}:")
        for meal_type, meal in day.items():
            if meal:
                meal_ingredients = MEALS[meal_type][meal]['ingredients']
                print(f"  {meal_type} - {meal}:")
                for ingredient, portion in meal_ingredients.items():
                    if ingredient not in ingredients:
                        ingredients[ingredient] = 0
                    old_amount = ingredients[ingredient]
                    ingredients[ingredient] += portion
                    print(f"    {ingredient}: +{portion} (total: {old_amount} → {ingredients[ingredient]})")
    
    print(f"\n🔍 DEBUG: Raw ingredient totals (before package conversion):")
    print("-" * 40)
    for ingredient, amount in sorted(ingredients.items()):
        print(f"  {ingredient}: {amount:.3f} portions")
    
    # Convert to actual packages needed
    final_ingredients = {}
    print(f"\n🔍 DEBUG: Package conversion:")
    print("-" * 40)
    for ingredient, amount in ingredients.items():
        package_count = calculate_needed_quantity(ingredient, amount, num_people)
        final_ingredients[ingredient] = package_count
        if ingredient in MEAL_PORTIONS:
            info = MEAL_PORTIONS[ingredient]
            print(f"  {ingredient}: {amount:.3f} portions × {num_people} people = {amount * num_people:.3f} total")
            print(f"    Package size: {info['size']} {info['unit']}, Servings per package: {info['servings']}")
            print(f"    Packages needed: {package_count}")
        else:
            print(f"  {ingredient}: {amount:.3f} portions → {package_count} packages (no portion data)")
    
    print("="*60)
    print()
    
    return final_ingredients, meal_plan

def display_recipe(meal_name: str, meal_type: str, num_people: int = 1):
    """Display recipe instructions for a given meal"""
    meal = MEALS[meal_type][meal_name]
    st.write("### Instructions:")
    for i, step in enumerate(meal['instructions'], 1):
        st.write(f"{i}. {step}")
    
    st.write(f"### Ingredients for {num_people} {'person' if num_people == 1 else 'people'}:")
    for ingredient, portion in meal['ingredients'].items():
        practical_amount = convert_to_practical_measurement(ingredient, portion, num_people)
        st.write(f"- {practical_amount}")

def generate_printable_plan(meal_plan, ingredients, unique_recipes, num_people, num_days):
    """Generate a PDF version of the meal plan, shopping list, and recipes"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    # Get styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30,
        alignment=1  # Center alignment
    )
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        spaceBefore=20
    )
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=8,
        spaceBefore=12
    )
    
    story = []
    
    # Title
    story.append(Paragraph(f"Two Week Meal Plan for {num_people} {'Person' if num_people == 1 else 'People'}", title_style))
    story.append(Spacer(1, 12))
    
    # Meal Plan Section
    story.append(Paragraph("MEAL PLAN", heading_style))
    
    for day_num in range(num_days):
        day_text = f"<b>Day {day_num + 1}:</b><br/>"
        for meal_type, meal in meal_plan[day_num].items():
            if meal:
                day_text += f"&nbsp;&nbsp;{meal_type}: {meal}<br/>"
            else:
                day_text += f"&nbsp;&nbsp;{meal_type}: <i>Please select more {meal_type.lower()} options</i><br/>"
        story.append(Paragraph(day_text, styles['Normal']))
        story.append(Spacer(1, 6))
    
    # Shopping List Section
    story.append(PageBreak())
    story.append(Paragraph("SHOPPING LIST", heading_style))
    
    shopping_text = ""
    for ingredient, quantity in sorted(ingredients.items()):
        if ingredient in MEAL_PORTIONS:
            info = MEAL_PORTIONS[ingredient]
            shopping_text += f"☐ {ingredient}: {quantity} × {info['size']} {info['unit']}<br/>"
        else:
            shopping_text += f"☐ {ingredient}: {quantity} units<br/>"
    
    story.append(Paragraph(shopping_text, styles['Normal']))
    
    # Recipes Section
    story.append(PageBreak())
    story.append(Paragraph("RECIPE COLLECTION", heading_style))
    
    # Sort recipes by meal type
    breakfast_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Breakfast']
    lunch_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Lunch']
    dinner_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Dinner']
    
    # Breakfast Recipes
    if breakfast_recipes:
        story.append(Paragraph("🌅 Breakfast Recipes", subheading_style))
        
        for meal, meal_type in sorted(breakfast_recipes):
            meal_data = MEALS[meal_type][meal]
            story.append(Paragraph(f"<b>{meal}</b>", styles['Heading4']))
            
            # Ingredients
            ingredients_text = f"<b>Ingredients (for {num_people} {'person' if num_people == 1 else 'people'}):</b><br/>"
            for ingredient, portion in meal_data['ingredients'].items():
                practical_amount = convert_to_practical_measurement(ingredient, portion, num_people)
                ingredients_text += f"• {practical_amount}<br/>"
            story.append(Paragraph(ingredients_text, styles['Normal']))
            
            # Instructions
            instructions_text = "<b>Instructions:</b><br/>"
            for i, step in enumerate(meal_data['instructions'], 1):
                instructions_text += f"{i}. {step}<br/>"
            story.append(Paragraph(instructions_text, styles['Normal']))
            story.append(Spacer(1, 12))
    
    # Lunch Recipes
    if lunch_recipes:
        story.append(PageBreak())
        story.append(Paragraph("🥪 Lunch Recipes", subheading_style))
        
        for meal, meal_type in sorted(lunch_recipes):
            meal_data = MEALS[meal_type][meal]
            story.append(Paragraph(f"<b>{meal}</b>", styles['Heading4']))
            
            # Ingredients
            ingredients_text = f"<b>Ingredients (for {num_people} {'person' if num_people == 1 else 'people'}):</b><br/>"
            for ingredient, portion in meal_data['ingredients'].items():
                practical_amount = convert_to_practical_measurement(ingredient, portion, num_people)
                ingredients_text += f"• {practical_amount}<br/>"
            story.append(Paragraph(ingredients_text, styles['Normal']))
            
            # Instructions
            instructions_text = "<b>Instructions:</b><br/>"
            for i, step in enumerate(meal_data['instructions'], 1):
                instructions_text += f"{i}. {step}<br/>"
            story.append(Paragraph(instructions_text, styles['Normal']))
            story.append(Spacer(1, 12))
    
    # Dinner Recipes
    if dinner_recipes:
        story.append(PageBreak())
        story.append(Paragraph("🍽️ Dinner Recipes", subheading_style))
        
        for meal, meal_type in sorted(dinner_recipes):
            meal_data = MEALS[meal_type][meal]
            story.append(Paragraph(f"<b>{meal}</b>", styles['Heading4']))
            
            # Ingredients
            ingredients_text = f"<b>Ingredients (for {num_people} {'person' if num_people == 1 else 'people'}):</b><br/>"
            for ingredient, portion in meal_data['ingredients'].items():
                practical_amount = convert_to_practical_measurement(ingredient, portion, num_people)
                ingredients_text += f"• {practical_amount}<br/>"
            story.append(Paragraph(ingredients_text, styles['Normal']))
            
            # Instructions
            instructions_text = "<b>Instructions:</b><br/>"
            for i, step in enumerate(meal_data['instructions'], 1):
                instructions_text += f"{i}. {step}<br/>"
            story.append(Paragraph(instructions_text, styles['Normal']))
            story.append(Spacer(1, 12))
    
    # Footer
    story.append(Spacer(1, 30))
    story.append(Paragraph("<i>Generated by Bishop's Storehouse Meal Planner</i>", styles['Normal']))
    
    # Build PDF
    doc.build(story)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    return pdf_bytes

def main():
    # Configure page to hide Streamlit menu elements
    st.set_page_config(
        page_title="Bishop's Storehouse Meal Planner",
        page_icon="🍽️",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': None
        }
    )
    
    # Hide Streamlit style elements
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    st.title("Two-Week Meal Planner")
    st.write("This planner helps you create a two-week meal plan using ingredients available at the Bishop's Storehouse.")
    
    num_people = st.number_input("Number of people in household:", min_value=1, max_value=10, value=4)
    
    st.header("Select Your Preferred Meals")
    
    selected_meals = []
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Breakfast Options")
        st.write("---")
        for meal in MEALS['Breakfast']:
            if st.checkbox(meal, key=f"breakfast_{meal}"):
                selected_meals.append(meal)

    
    with col2:
        st.subheader("Lunch Options")
        st.write("---")
        for meal in MEALS['Lunch']:
            if st.checkbox(meal, key=f"lunch_{meal}"):
                selected_meals.append(meal)

    
    with col3:
        st.subheader("Dinner Options")
        st.write("---")
        for meal in MEALS['Dinner']:
            if st.checkbox(meal, key=f"dinner_{meal}"):
                selected_meals.append(meal)

               
    
    st.write("")
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_plan = st.button("Generate Meal Plan", key="generate_plan_button")
    
    if generate_plan and selected_meals:
        num_days = 14  # Two weeks
        
        ingredients, meal_plan = calculate_ingredients(selected_meals, num_people, num_days)
        
        st.header("Two Week Meal Plan")
        
        # Display meal plan in a clean, easy-to-read format
        for day_num in range(0, num_days, 2):
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(f"Day {day_num + 1}")
                for meal_type, meal in meal_plan[day_num].items():
                    if meal:
                        st.write(f"**{meal_type}:** {meal}")
                    else:
                        st.write(f"**{meal_type}:** *Please select more {meal_type.lower()} options*")
                st.write("")  # Add some spacing
            
            if day_num + 1 < num_days:
                with col2:
                    st.subheader(f"Day {day_num + 2}")
                    for meal_type, meal in meal_plan[day_num + 1].items():
                        if meal:
                            st.write(f"**{meal_type}:** {meal}")
                        else:
                            st.write(f"**{meal_type}:** *Please select more {meal_type.lower()} options*")
                    st.write("")  # Add some spacing
        
        st.header("Shopping List")
        st.write("Based on your meal plan, here are the quantities needed:")
        for ingredient, quantity in ingredients.items():
            if ingredient in MEAL_PORTIONS:
                info = MEAL_PORTIONS[ingredient]
                st.write(f"- **{ingredient}:** {quantity} × {info['size']} {info['unit']}")
            else:
                st.write(f"- **{ingredient}:** {quantity} units")
        
        # Collect all unique recipes used in the meal plan
        st.header("📖 Recipe Collection")
        st.write("Here are all the recipes you'll need for your meal plan:")
        
        unique_recipes = set()
        for day in meal_plan:
            for meal_type, meal in day.items():
                if meal:
                    unique_recipes.add((meal, meal_type))
        
        # Sort recipes by meal type for better organization
        breakfast_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Breakfast']
        lunch_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Lunch']
        dinner_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Dinner']
        
        # Display recipes by category
        if breakfast_recipes:
            st.subheader("🌅 Breakfast Recipes")
            for meal, meal_type in sorted(breakfast_recipes):
                with st.expander(f"{meal}"):
                    display_recipe(meal, meal_type, num_people)
        
        if lunch_recipes:
            st.subheader("🥪 Lunch Recipes")
            for meal, meal_type in sorted(lunch_recipes):
                with st.expander(f"{meal}"):
                    display_recipe(meal, meal_type, num_people)
        
        if dinner_recipes:
            st.subheader("🍽️ Dinner Recipes")
            for meal, meal_type in sorted(dinner_recipes):
                with st.expander(f"{meal}"):
                    display_recipe(meal, meal_type, num_people)
        
        # Add print/download functionality
        st.write("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            pdf_content = generate_printable_plan(meal_plan, ingredients, unique_recipes, num_people, num_days)
            st.download_button(
                label="📄 Download PDF Meal Plan",
                data=pdf_content,
                file_name=f"meal_plan_{num_people}_people.pdf",
                mime="application/pdf",
                key="download_plan"
            )
        
        if len(selected_meals) < 6:
            st.warning("Consider selecting more meals for better variety in your meal plan!")
    
    elif generate_plan and not selected_meals:
        st.error("Please select at least one meal before generating the plan!")

if __name__ == "__main__":
    main()