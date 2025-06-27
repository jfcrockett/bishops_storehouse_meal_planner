import streamlit as st
import random
from typing import List, Dict

# Define package sizes and realistic servings per package
MEAL_PORTIONS = {
    'fully cooked beef': {'size': 14.4, 'servings': 2, 'unit': 'oz'},
    'beef stew': {'size': 14.4, 'servings': 2, 'unit': 'oz'},
    'chili': {'size': 14.4, 'servings': 2, 'unit': 'oz'},
    'pork and beans': {'size': 14.8, 'servings': 2, 'unit': 'oz'},
    'tuna': {'size': 5, 'servings': 2, 'unit': 'oz'},
    'chicken breast pieces': {'size': 12.5, 'servings': 2, 'unit': 'oz'},
    'chicken rotini soup': {'size': 14.4, 'servings': 2, 'unit': 'oz'},
    'cream of chicken soup': {'size': 14.5, 'servings': 2, 'unit': 'oz'},
    'cream of mushroom soup': {'size': 14.5, 'servings': 2, 'unit': 'oz'},
    'tomato soup': {'size': 14.4, 'servings': 2, 'unit': 'oz'},
    'applesauce': {'size': 26.5, 'servings': 6, 'unit': 'oz'},
    'peaches': {'size': 29, 'servings': 6, 'unit': 'oz'},
    'pears': {'size': 29, 'servings': 6, 'unit': 'oz'},
    'corn': {'size': 14.4, 'servings': 3, 'unit': 'oz'},
    'green beans': {'size': 14.4, 'servings': 3, 'unit': 'oz'},
    'spaghetti sauce': {'size': 27.7, 'servings': 4, 'unit': 'oz'},
    'diced tomatoes': {'size': 28, 'servings': 4, 'unit': 'oz'},
    'black beans': {'size': 14.8, 'servings': 3, 'unit': 'oz'},
    'white beans': {'size': 14.8, 'servings': 3, 'unit': 'oz'},
    'refried beans': {'size': 32, 'servings': 6, 'unit': 'oz'},
    'instant potatoes': {'size': 28, 'servings': 8, 'unit': 'oz'},
    'rice': {'size': 32, 'servings': 12, 'unit': 'oz'},
    'honey': {'size': 12, 'servings': 24, 'unit': 'oz'},
    'raspberry jam': {'size': 20.5, 'servings': 24, 'unit': 'oz'},
    'peanut butter': {'size': 16, 'servings': 24, 'unit': 'oz'},
    'mayo': {'size': 15, 'servings': 24, 'unit': 'oz'},
    'ranch dressing': {'size': 16, 'servings': 24, 'unit': 'oz'},
    'salsa': {'size': 26.5, 'servings': 8, 'unit': 'oz'},
    'pancake mix': {'size': 64, 'servings': 24, 'unit': 'oz'},
    'macaroni': {'size': 16, 'servings': 6, 'unit': 'oz'},
    'macaroni and cheese': {'size': 7, 'servings': 2, 'unit': 'oz'},
    'spaghetti': {'size': 16, 'servings': 6, 'unit': 'oz'},
    'rolled oats': {'size': 32, 'servings': 12, 'unit': 'oz'},
    'honey nut o\'s': {'size': 24.5, 'servings': 8, 'unit': 'oz'},
    'raisin bran': {'size': 22, 'servings': 8, 'unit': 'oz'},
    'bread': {'size': 20, 'servings': 10, 'unit': 'slices'},
    'hot dog buns': {'size': 8, 'servings': 4, 'unit': 'buns'},
    'tortillas': {'size': 12, 'servings': 6, 'unit': 'count'},
    'eggs': {'size': 12, 'servings': 4, 'unit': 'count'},
    'butter': {'size': 16, 'servings': 32, 'unit': 'oz'},
    'milk': {'size': 128, 'servings': 16, 'unit': 'oz'},
    'cheddar cheese': {'size': 16, 'servings': 8, 'unit': 'oz'},
    'vanilla yogurt': {'size': 16, 'servings': 8, 'unit': 'oz'},
    'raisins': {'size': 16, 'servings': 16, 'unit': 'oz'},
    'cinnamon': {'size': 2.37, 'servings': 24, 'unit': 'oz'}
}

# Define all meals with ingredients and instructions
MEALS = {
    'Breakfast': {
        'Classic Oatmeal with Fruit': {
            'ingredients': {
                'rolled oats': 1/12,
                'milk': 1/16,
                'peaches': 1/6,
                'honey': 1/24,
                'cinnamon': 1/24
            },
            'instructions': [
                "Cook oats with milk according to package directions",
                "Drain and chop peaches into small pieces",
                "Stir peaches into hot oatmeal",
                "Drizzle with honey and sprinkle with cinnamon",
                "Let cool slightly before serving"
            ]
        },
        'Fluffy Pancakes with Peaches': {
            'ingredients': {
                'pancake mix': 1/24,
                'eggs': 1/4,
                'milk': 1/16,
                'butter': 1/32,
                'peaches': 1/6,
                'honey': 1/24
            },
            'instructions': [
                "Mix pancake mix, eggs, and milk until just combined",
                "Heat butter in a pan over medium heat",
                "Pour 1/4 cup batter for each pancake",
                "Cook until bubbles form, then flip and cook until golden",
                "Serve topped with drained peaches and honey"
            ]
        },
        'Honey Nut Cereal Bowl': {
            'ingredients': {
                'honey nut o\'s': 1/8,
                'milk': 1/16,
                'peaches': 1/6
            },
            'instructions': [
                "Pour cereal into a bowl",
                "Add cold milk",
                "Drain and chop peaches",
                "Top cereal with peach pieces",
                "Serve immediately"
            ]
        },
        'Scrambled Eggs & Toast': {
            'ingredients': {
                'eggs': 1/4,
                'butter': 1/32,
                'bread': 2/10,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Beat eggs in a bowl",
                "Heat butter in a pan over low heat",
                "Add eggs and scramble gently until set",
                "Toast bread slices",
                "Serve eggs over toast, topped with cheese"
            ]
        },
        'Peanut Butter Honey Toast': {
            'ingredients': {
                'bread': 2/10,
                'peanut butter': 1/24,
                'honey': 1/24
            },
            'instructions': [
                "Toast bread slices until golden",
                "Spread peanut butter evenly on warm toast",
                "Drizzle honey over peanut butter",
                "Cut diagonally and serve immediately"
            ]
        },
        'Yogurt Parfait with Fruit': {
            'ingredients': {
                'vanilla yogurt': 1/8,
                'peaches': 1/6,
                'honey': 1/24,
                'raisins': 1/16
            },
            'instructions': [
                "Drain and chop peaches",
                "Layer yogurt and peaches in a bowl",
                "Sprinkle raisins on top",
                "Drizzle with honey",
                "Serve chilled"
            ]
        }
    },
    'Lunch': {
        'Classic Tuna Sandwich': {
            'ingredients': {
                'tuna': 1/2,
                'mayo': 1/24,
                'bread': 2/10
            },
            'instructions': [
                "Drain tuna completely",
                "Mix tuna with mayo until well combined",
                "Spread mixture evenly on bread",
                "Top with second slice of bread",
                "Cut in half and serve"
            ]
        },
        'Grilled Cheese & Tomato Soup': {
            'ingredients': {
                'bread': 2/10,
                'cheddar cheese': 1/8,
                'butter': 1/32,
                'tomato soup': 1/2
            },
            'instructions': [
                "Heat tomato soup according to package directions",
                "Butter outside of bread slices",
                "Place cheese between bread (butter side out)",
                "Cook in pan until golden and cheese melts",
                "Serve hot with soup"
            ]
        },
        'Mexican Rice & Bean Bowl': {
            'ingredients': {
                'rice': 1/12,
                'black beans': 1/3,
                'corn': 1/3,
                'salsa': 1/8,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Cook rice according to package directions",
                "Heat black beans and corn",
                "Layer rice in bowl",
                "Top with beans, corn, salsa, and cheese",
                "Serve warm"
            ]
        },
        'Cheese Quesadilla': {
            'ingredients': {
                'tortillas': 2/6,
                'cheddar cheese': 1/8,
                'salsa': 1/8
            },
            'instructions': [
                "Sprinkle cheese on one tortilla",
                "Top with second tortilla",
                "Cook in dry pan until golden and cheese melts",
                "Flip once during cooking",
                "Cut into wedges and serve with salsa"
            ]
        },
        'Creamy Macaroni & Cheese': {
            'ingredients': {
                'macaroni and cheese': 1/2,
                'milk': 1/16,
                'butter': 1/32
            },
            'instructions': [
                "Cook macaroni according to package directions",
                "Drain and return to pot",
                "Add cheese packet, milk, and butter",
                "Stir until creamy and well combined",
                "Serve hot"
            ]
        },
        'Chicken Noodle Soup with Bread': {
            'ingredients': {
                'chicken rotini soup': 1/2,
                'bread': 1/10,
                'butter': 1/32
            },
            'instructions': [
                "Heat soup according to package directions",
                "Toast bread and spread with butter",
                "Serve soup hot with buttered toast",
                "Dip bread in soup if desired"
            ]
        },
        'PB&J Sandwich': {
            'ingredients': {
                'bread': 2/10,
                'peanut butter': 1/24,
                'raspberry jam': 1/24
            },
            'instructions': [
                "Spread peanut butter on one slice of bread",
                "Spread jam on the other slice",
                "Press slices together",
                "Cut diagonally if desired",
                "Serve immediately"
            ]
        },
        'Chicken Salad Sandwich': {
            'ingredients': {
                'chicken breast pieces': 1/2,
                'mayo': 1/24,
                'bread': 2/10
            },
            'instructions': [
                "Drain chicken and chop into small pieces",
                "Mix with mayo until well combined",
                "Spread on bread slices",
                "Top with second slice",
                "Cut and serve"
            ]
        },
        'Bean & Corn Salad': {
            'ingredients': {
                'black beans': 1/3,
                'white beans': 1/3,
                'corn': 1/3,
                'ranch dressing': 1/24
            },
            'instructions': [
                "Drain and rinse all beans and corn",
                "Combine in a large bowl",
                "Add ranch dressing and toss well",
                "Chill for better flavor if time allows",
                "Serve cold"
            ]
        },
        'Chicken & Cheese Wrap': {
            'ingredients': {
                'tortillas': 1/6,
                'chicken breast pieces': 1/2,
                'cheddar cheese': 1/8,
                'ranch dressing': 1/24
            },
            'instructions': [
                "Warm tortilla slightly",
                "Spread ranch dressing on tortilla",
                "Add drained chicken and cheese",
                "Roll up tightly",
                "Cut in half and serve"
            ]
        }
    },
    'Dinner': {
        'Spaghetti with Meat Sauce': {
            'ingredients': {
                'spaghetti': 1/6,
                'spaghetti sauce': 1/4,
                'fully cooked beef': 1/2
            },
            'instructions': [
                "Cook spaghetti according to package directions",
                "Heat beef in a large pan",
                "Add spaghetti sauce to beef and simmer 5 minutes",
                "Drain pasta and add to sauce",
                "Toss well and serve hot"
            ]
        },
        'Beef & Rice Power Bowl': {
            'ingredients': {
                'rice': 1/12,
                'fully cooked beef': 1/2,
                'corn': 1/3,
                'black beans': 1/3,
                'salsa': 1/8,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Cook rice according to package directions",
                "Heat beef, corn, and black beans separately",
                "Layer rice in bowls",
                "Top with beef, vegetables, salsa, and cheese",
                "Serve immediately while hot"
            ]
        },
        'Chicken & Rice Casserole': {
            'ingredients': {
                'chicken breast pieces': 1/2,
                'rice': 1/12,
                'cream of chicken soup': 1/2,
                'corn': 1/3,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Cook rice according to package directions",
                "Mix rice, chicken, soup, and corn in a baking dish",
                "Top with shredded cheese",
                "Bake or heat until bubbly and cheese melts",
                "Let stand 5 minutes before serving"
            ]
        },
        'Hearty Chili with Bread': {
            'ingredients': {
                'chili': 1/2,
                'bread': 2/10,
                'cheddar cheese': 1/8,
                'butter': 1/32
            },
            'instructions': [
                "Heat chili in a pot until hot",
                "Toast bread and spread with butter",
                "Serve chili in bowls topped with cheese",
                "Serve with buttered toast on the side"
            ]
        },
        'Beef Stew with Mashed Potatoes': {
            'ingredients': {
                'beef stew': 1/2,
                'instant potatoes': 1/8,
                'butter': 1/32,
                'milk': 1/16
            },
            'instructions': [
                "Heat beef stew according to directions",
                "Prepare instant potatoes with milk and butter",
                "Serve stew over mashed potatoes",
                "Let stand briefly before serving"
            ]
        },
        'Tuna Noodle Casserole': {
            'ingredients': {
                'macaroni': 1/6,
                'tuna': 1/2,
                'cream of mushroom soup': 1/2,
                'green beans': 1/3,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Cook macaroni according to package directions",
                "Mix drained tuna, soup, and green beans",
                "Add cooked macaroni and stir gently",
                "Top with cheese and heat until melted",
                "Serve hot"
            ]
        },
        'Bean & Cheese Burritos': {
            'ingredients': {
                'tortillas': 2/6,
                'refried beans': 1/6,
                'rice': 1/12,
                'cheddar cheese': 1/8,
                'salsa': 1/8
            },
            'instructions': [
                "Cook rice according to package directions",
                "Heat refried beans until warm",
                "Warm tortillas",
                "Fill with beans, rice, and cheese",
                "Roll up and serve with salsa"
            ]
        },
        'Chicken Pot Pie Bowl': {
            'ingredients': {
                'chicken breast pieces': 1/2,
                'cream of chicken soup': 1/2,
                'corn': 1/3,
                'green beans': 1/3,
                'instant potatoes': 1/8
            },
            'instructions': [
                "Heat chicken, soup, corn, and green beans together",
                "Prepare instant potatoes according to package",
                "Serve chicken mixture in bowls",
                "Top with a scoop of mashed potatoes",
                "Serve immediately"
            ]
        },
        'Shepherd\'s Pie': {
            'ingredients': {
                'fully cooked beef': 1/2,
                'corn': 1/3,
                'green beans': 1/3,
                'instant potatoes': 1/8,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Heat beef with corn and green beans",
                "Prepare instant potatoes according to package",
                "Layer beef mixture in bottom of dish",
                "Top with mashed potatoes and cheese",
                "Heat until cheese melts"
            ]
        },
        'Cheesy Bean Enchiladas': {
            'ingredients': {
                'tortillas': 3/6,
                'refried beans': 1/6,
                'black beans': 1/3,
                'cheddar cheese': 1/8,
                'salsa': 1/8
            },
            'instructions': [
                "Mix refried beans with drained black beans",
                "Fill tortillas with bean mixture and some cheese",
                "Roll up and place in baking dish",
                "Top with remaining cheese and salsa",
                "Heat until cheese melts and serve hot"
            ]
        }
    }
}

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
    ingredients = {}
    meal_plan = []
    
    # Create meal plan
    for _ in range(num_days):
        day_meals = {
            'Breakfast': [],
            'Lunch': [],
            'Dinner': []
        }
        for meal_type, meals in MEALS.items():
            available_meals = [m for m in selected_meals if m in meals]
            if available_meals:
                day_meals[meal_type] = random.choice(available_meals)
        meal_plan.append(day_meals)
    
    # Calculate ingredients
    for day in meal_plan:
        for meal_type, meal in day.items():
            if meal:
                meal_ingredients = MEALS[meal_type][meal]['ingredients']
                for ingredient, portion in meal_ingredients.items():
                    if ingredient not in ingredients:
                        ingredients[ingredient] = 0
                    ingredients[ingredient] += portion
    
    # Convert to actual packages needed
    final_ingredients = {}
    for ingredient, amount in ingredients.items():
        final_ingredients[ingredient] = calculate_needed_quantity(ingredient, amount, num_people)
    
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
    """Generate a printable version of the meal plan, shopping list, and recipes"""
    content = []
    
    # Header
    content.append("=" * 60)
    content.append(f"TWO WEEK MEAL PLAN FOR {num_people} {'PERSON' if num_people == 1 else 'PEOPLE'}")
    content.append("=" * 60)
    content.append("")
    
    # Meal Plan
    content.append("MEAL PLAN")
    content.append("-" * 20)
    content.append("")
    
    for day_num in range(num_days):
        content.append(f"DAY {day_num + 1}:")
        for meal_type, meal in meal_plan[day_num].items():
            if meal:
                content.append(f"  {meal_type}: {meal}")
            else:
                content.append(f"  {meal_type}: *Please select more {meal_type.lower()} options*")
        content.append("")
    
    # Shopping List
    content.append("SHOPPING LIST")
    content.append("-" * 20)
    content.append("")
    
    for ingredient, quantity in sorted(ingredients.items()):
        if ingredient in MEAL_PORTIONS:
            info = MEAL_PORTIONS[ingredient]
            content.append(f"☐ {ingredient}: {quantity} × {info['size']} {info['unit']}")
        else:
            content.append(f"☐ {ingredient}: {quantity} units")
    content.append("")
    
    # Recipes
    content.append("RECIPE COLLECTION")
    content.append("-" * 20)
    content.append("")
    
    # Sort recipes by meal type
    breakfast_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Breakfast']
    lunch_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Lunch']
    dinner_recipes = [(meal, meal_type) for meal, meal_type in unique_recipes if meal_type == 'Dinner']
    
    # Breakfast Recipes
    if breakfast_recipes:
        content.append("BREAKFAST RECIPES")
        content.append("~" * 18)
        content.append("")
        
        for meal, meal_type in sorted(breakfast_recipes):
            meal_data = MEALS[meal_type][meal]
            content.append(f"{meal.upper()}")
            content.append("")
            
            content.append(f"Ingredients (for {num_people} {'person' if num_people == 1 else 'people'}):")
            for ingredient, portion in meal_data['ingredients'].items():
                practical_amount = convert_to_practical_measurement(ingredient, portion, num_people)
                content.append(f"  • {practical_amount}")
            content.append("")
            
            content.append("Instructions:")
            for i, step in enumerate(meal_data['instructions'], 1):
                content.append(f"  {i}. {step}")
            content.append("")
            content.append("-" * 40)
            content.append("")
    
    # Lunch Recipes
    if lunch_recipes:
        content.append("LUNCH RECIPES")
        content.append("~" * 14)
        content.append("")
        
        for meal, meal_type in sorted(lunch_recipes):
            meal_data = MEALS[meal_type][meal]
            content.append(f"{meal.upper()}")
            content.append("")
            
            content.append(f"Ingredients (for {num_people} {'person' if num_people == 1 else 'people'}):")
            for ingredient, portion in meal_data['ingredients'].items():
                practical_amount = convert_to_practical_measurement(ingredient, portion, num_people)
                content.append(f"  • {practical_amount}")
            content.append("")
            
            content.append("Instructions:")
            for i, step in enumerate(meal_data['instructions'], 1):
                content.append(f"  {i}. {step}")
            content.append("")
            content.append("-" * 40)
            content.append("")
    
    # Dinner Recipes
    if dinner_recipes:
        content.append("DINNER RECIPES")
        content.append("~" * 14)
        content.append("")
        
        for meal, meal_type in sorted(dinner_recipes):
            meal_data = MEALS[meal_type][meal]
            content.append(f"{meal.upper()}")
            content.append("")
            
            content.append(f"Ingredients (for {num_people} {'person' if num_people == 1 else 'people'}):")
            for ingredient, portion in meal_data['ingredients'].items():
                practical_amount = convert_to_practical_measurement(ingredient, portion, num_people)
                content.append(f"  • {practical_amount}")
            content.append("")
            
            content.append("Instructions:")
            for i, step in enumerate(meal_data['instructions'], 1):
                content.append(f"  {i}. {step}")
            content.append("")
            content.append("-" * 40)
            content.append("")
    
    content.append("=" * 60)
    content.append("Generated by Bishop's Storehouse Meal Planner")
    content.append("=" * 60)
    
    return "\n".join(content)

def main():
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
            if st.button("📄 Download Printable Meal Plan", key="download_plan"):
                printable_content = generate_printable_plan(meal_plan, ingredients, unique_recipes, num_people, num_days)
                st.download_button(
                    label="💾 Download as Text File",
                    data=printable_content,
                    file_name=f"meal_plan_{num_people}_people.txt",
                    mime="text/plain"
                )
        
        if len(selected_meals) < 6:
            st.warning("Consider selecting more meals for better variety in your meal plan!")
    
    elif generate_plan and not selected_meals:
        st.error("Please select at least one meal before generating the plan!")

if __name__ == "__main__":
    main()