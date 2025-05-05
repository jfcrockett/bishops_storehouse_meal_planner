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
        'Berry Oatmeal Bowl': {
            'ingredients': {
                'rolled oats': 1/12,
                'milk': 1/16,
                'raspberry jam': 1/24,
                'honey': 1/24,
                'cinnamon': 1/24
            },
            'instructions': [
                "Heat milk until warm (stovetop or microwave)",
                "Add oats and cook until soft, about 5 minutes",
                "Stir in a small spoonful of raspberry jam",
                "Drizzle with honey and sprinkle with cinnamon",
                "Let stand for 1 minute before serving"
            ]
        },
        'Peanut Butter Toast with Honey': {
            'ingredients': {
                'bread': 2/10,
                'peanut butter': 1/24,
                'honey': 1/24,
                'cinnamon': 1/24
            },
            'instructions': [
                "Toast bread slices",
                "Spread peanut butter on warm toast",
                "Drizzle honey over peanut butter",
                "Sprinkle lightly with cinnamon",
                "Cut into triangles if desired"
            ]
        },
        'Cereal Breakfast Medley': {
            'ingredients': {
                'honey nut o\'s': 1/8,
                'raisin bran': 1/8,
                'milk': 1/16,
                'peaches': 1/6
            },
            'instructions': [
                "Mix both cereals in a bowl",
                "Drain peaches, reserving 2 tbsp juice",
                "Chop peaches into small pieces",
                "Add peaches with reserved juice to cereal",
                "Pour milk over the mixture and enjoy"
            ]
        },
        'Savory Breakfast Bowl': {
            'ingredients': {
                'eggs': 1/4,
                'rice': 1/12,
                'cheddar cheese': 1/8,
                'salsa': 1/8
            },
            'instructions': [
                "Cook rice according to package directions",
                "Scramble eggs in a pan until just set",
                "Place hot rice in a bowl",
                "Top with scrambled eggs",
                "Add shredded cheese and salsa on top"
            ]
        },
        'Pancakes with Fruit Topping': {
            'ingredients': {
                'pancake mix': 1/24,
                'eggs': 1/4,
                'milk': 1/16,
                'butter': 1/32,
                'peaches': 1/6
            },
            'instructions': [
                "Mix pancake mix, eggs, and milk until just combined",
                "Heat a pan and add a small amount of butter",
                "Pour about 1/4 cup batter for each pancake",
                "Cook until bubbles form, then flip",
                "Drain and chop peaches to serve on top"
            ]
        }
    },
    'Lunch': {
        'Tuna Melt': {
            'ingredients': {
                'tuna': 1/2,
                'bread': 2/10,
                'mayo': 1/24,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Drain tuna well and mix with mayo",
                "Spread tuna mixture on bread slices",
                "Top with sliced or shredded cheese",
                "Toast in oven or pan until cheese melts",
                "Let cool slightly before serving"
            ]
        },
        'Black Bean & Rice Bowl': {
            'ingredients': {
                'black beans': 1/3,
                'rice': 1/12,
                'corn': 1/3,
                'salsa': 1/8,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Heat black beans in a pan",
                "Prepare rice according to package directions",
                "Heat corn separately",
                "Layer rice, beans, and corn in a bowl",
                "Top with salsa and shredded cheese"
            ]
        },
        'Chicken Tortilla Soup': {
            'ingredients': {
                'chicken rotini soup': 1/2,
                'tortillas': 1/6,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Heat soup in a saucepan until hot",
                "Cut 1-2 tortillas into strips",
                "Top hot soup with tortilla strips",
                "Sprinkle with shredded cheese",
                "Let stand 1 minute before serving"
            ]
        },
        'Bean & Cheese Quesadilla': {
            'ingredients': {
                'tortillas': 2/6,
                'refried beans': 1/6,
                'cheddar cheese': 1/8,
                'salsa': 1/8
            },
            'instructions': [
                "Spread refried beans on one tortilla",
                "Sprinkle cheese on top of beans",
                "Cover with second tortilla",
                "Heat in a dry pan until golden and cheese melts",
                "Cut into wedges and serve with salsa"
            ]
        },
        'Macaroni & Cheese with Tuna': {
            'ingredients': {
                'macaroni and cheese': 1/2,
                'tuna': 1/2
            },
            'instructions': [
                "Prepare macaroni and cheese according to package directions",
                "Drain tuna well",
                "Mix tuna into prepared macaroni and cheese",
                "Heat for 1 more minute to warm through",
                "Let stand briefly before serving"
            ]
        },
        'Tomato Soup & Grilled Cheese': {
            'ingredients': {
                'tomato soup': 1/2,
                'bread': 2/10,
                'cheddar cheese': 1/8,
                'butter': 1/32
            },
            'instructions': [
                "Heat tomato soup according to directions",
                "Butter outside of bread slices",
                "Place cheese between bread slices (butter side out)",
                "Cook sandwich in pan until golden and cheese melts",
                "Serve with hot soup"
            ]
        },
        'Rice & Bean Salad': {
            'ingredients': {
                'rice': 1/12,
                'black beans': 1/6,
                'white beans': 1/6,
                'corn': 1/3,
                'ranch dressing': 1/24
            },
            'instructions': [
                "Cook rice and allow to cool",
                "Drain and rinse beans and corn",
                "Mix rice, beans, and corn in a bowl",
                "Add ranch dressing and toss to coat",
                "Chill before serving if possible"
            ]
        },
        'Peanut Butter & Jam Sandwich': {
            'ingredients': {
                'bread': 2/10,
                'peanut butter': 1/24,
                'raspberry jam': 1/24
            },
            'instructions': [
                "Spread peanut butter on one slice of bread",
                "Spread raspberry jam on the other slice",
                "Put slices together",
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
                "Drain chicken pieces well",
                "Chop chicken into smaller pieces if needed",
                "Mix with mayo until well combined",
                "Spread on bread slices",
                "Top with second bread slice"
            ]
        },
        'Egg Salad Sandwich': {
            'ingredients': {
                'eggs': 1/4,
                'mayo': 1/24,
                'bread': 2/10
            },
            'instructions': [
                "Hard boil eggs, cool, peel and chop",
                "Mix chopped eggs with mayo",
                "Add salt and pepper if available",
                "Spread on bread slices",
                "Top with second slice of bread"
            ]
        }
    },
    'Dinner': {
        'Beef & Bean Burrito Bowl': {
            'ingredients': {
                'rice': 1/12,
                'fully cooked beef': 1/2,
                'black beans': 1/3,
                'corn': 1/3,
                'salsa': 1/8,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Cook rice according to package directions",
                "Heat beef in a pan",
                "Warm beans and corn separately",
                "Arrange rice in bowl, top with beef, beans, and corn",
                "Finish with salsa and shredded cheese"
            ]
        },
        'Spaghetti with Meat Sauce': {
            'ingredients': {
                'spaghetti': 1/6,
                'spaghetti sauce': 1/4,
                'fully cooked beef': 1/2
            },
            'instructions': [
                "Cook spaghetti according to package directions",
                "Heat beef in a pan",
                "Add spaghetti sauce to beef and heat through",
                "Drain pasta and return to pot",
                "Pour meat sauce over pasta and toss to combine"
            ]
        },
        'Chicken & Rice Casserole': {
            'ingredients': {
                'chicken breast pieces': 1/2,
                'rice': 1/12,
                'cream of chicken soup': 1/2,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Cook rice according to package directions",
                "Mix cooked rice with cream of chicken soup",
                "Add drained chicken pieces and stir gently",
                "Top with shredded cheese",
                "Heat until bubbly and cheese is melted"
            ]
        },
        'Shepherd\'s Pie': {
            'ingredients': {
                'instant potatoes': 1/8,
                'fully cooked beef': 1/2,
                'corn': 1/3,
                'green beans': 1/3
            },
            'instructions': [
                "Heat beef with drained vegetables",
                "Prepare instant potatoes according to package",
                "Place beef and vegetable mixture in a dish or bowl",
                "Top with prepared mashed potatoes",
                "Heat until hot throughout"
            ]
        },
        'White Bean Chicken Chili': {
            'ingredients': {
                'white beans': 1/3,
                'chicken breast pieces': 1/2,
                'corn': 1/3,
                'salsa': 1/8
            },
            'instructions': [
                "Combine white beans (with liquid) and drained chicken in pot",
                "Add corn and salsa",
                "Bring to a simmer and cook for 10 minutes",
                "Stir occasionally to prevent sticking",
                "Let stand 5 minutes before serving"
            ]
        },
        'Beef Stew with Rice': {
            'ingredients': {
                'beef stew': 1/2,
                'rice': 1/12
            },
            'instructions': [
                "Prepare rice according to package directions",
                "Heat beef stew in a separate pot",
                "Serve stew over rice",
                "Let stand for 1 minute before serving",
                "Stir gently if desired"
            ]
        },
        'Tuna Noodle Casserole': {
            'ingredients': {
                'macaroni': 1/6,
                'tuna': 1/2,
                'cream of mushroom soup': 1/2,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Cook macaroni according to package directions",
                "Mix drained tuna with cream of mushroom soup",
                "Add cooked macaroni and stir gently",
                "Top with shredded cheese",
                "Heat until bubbly and cheese is melted"
            ]
        },
        'Mexican Bean Enchiladas': {
            'ingredients': {
                'tortillas': 2/6,
                'refried beans': 1/6,
                'black beans': 1/3,
                'salsa': 1/8,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Mix refried beans with drained black beans",
                "Spread bean mixture onto tortillas",
                "Roll up tortillas and place in dish",
                "Top with salsa and cheese",
                "Heat until cheese melts"
            ]
        },
        'Chicken Pot Pie Bowl': {
            'ingredients': {
                'chicken breast pieces': 1/2,
                'cream of chicken soup': 1/2,
                'corn': 1/6,
                'green beans': 1/6,
                'instant potatoes': 1/8
            },
            'instructions': [
                "Mix chicken pieces, soup, and drained vegetables in a pot",
                "Heat mixture until bubbly",
                "Prepare instant potatoes according to package",
                "Serve chicken mixture in bowls topped with mashed potatoes",
                "Let stand briefly before serving"
            ]
        },
        'Chili Mac': {
            'ingredients': {
                'chili': 1/2,
                'macaroni': 1/6,
                'cheddar cheese': 1/8
            },
            'instructions': [
                "Cook macaroni according to package directions",
                "Heat chili in a separate pot",
                "Drain macaroni and add to chili",
                "Stir in half the cheese until melted",
                "Top with remaining cheese before serving"
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
        final_ingredients[ingredient] = calculate_needed_quantity(ingredient, amount * num_days, num_people)
    
    return final_ingredients, meal_plan

def display_recipe(meal_name: str, meal_type: str):
    """Display recipe instructions for a given meal"""
    meal = MEALS[meal_type][meal_name]
    st.write("### Instructions:")
    for i, step in enumerate(meal['instructions'], 1):
        st.write(f"{i}. {step}")
    
    st.write("### Ingredients per person:")
    for ingredient, portion in meal['ingredients'].items():
        if ingredient in MEAL_PORTIONS:
            info = MEAL_PORTIONS[ingredient]
            amount = portion * info['size']
            st.write(f"- {ingredient}: {amount:.1f} {info['unit']}")
        else:
            st.write(f"- {ingredient}: {portion} portion")

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
                with st.expander("See Recipe"):
                    display_recipe(meal, 'Breakfast')
    
    with col2:
        st.subheader("Lunch Options")
        st.write("---")
        for meal in MEALS['Lunch']:
            if st.checkbox(meal, key=f"lunch_{meal}"):
                selected_meals.append(meal)
                with st.expander("See Recipe"):
                    display_recipe(meal, 'Lunch')
    
    with col3:
        st.subheader("Dinner Options")
        st.write("---")
        for meal in MEALS['Dinner']:
            if st.checkbox(meal, key=f"dinner_{meal}"):
                selected_meals.append(meal)
                with st.expander("See Recipe"):
                    display_recipe(meal, 'Dinner')
    
    st.write("")
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_plan = st.button("Generate Meal Plan", key="generate_plan_button")
    
    if generate_plan and selected_meals:
        num_days = 14  # Two weeks
        
        ingredients, meal_plan = calculate_ingredients(selected_meals, num_people, num_days)
        
        st.header("Two Week Meal Plan")
        
        for day_num in range(0, num_days, 2):
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(f"Day {day_num + 1}")
                for meal_type, meal in meal_plan[day_num].items():
                    if meal:
                        st.write(f"**{meal_type}:** {meal}")
                        with st.expander("See Recipe"):
                            display_recipe(meal, meal_type)
                    else:
                        st.write(f"**{meal_type}:** *Please select more {meal_type.lower()} options*")
            
            if day_num + 1 < num_days:
                with col2:
                    st.subheader(f"Day {day_num + 2}")
                    for meal_type, meal in meal_plan[day_num + 1].items():
                        if meal:
                            st.write(f"**{meal_type}:** {meal}")
                            with st.expander("See Recipe"):
                                display_recipe(meal, meal_type)
                        else:
                            st.write(f"**{meal_type}:** *Please select more {meal_type.lower()} options*")
        
        st.header("Shopping List")
        st.write("Based on your meal plan, here are the quantities needed:")
        for ingredient, quantity in ingredients.items():
            if ingredient in MEAL_PORTIONS:
                info = MEAL_PORTIONS[ingredient]
                st.write(f"- **{ingredient}:** {quantity} × {info['size']} {info['unit']}")
            else:
                st.write(f"- **{ingredient}:** {quantity} units")
        
        if len(selected_meals) < 6:
            st.warning("Consider selecting more meals for better variety in your meal plan!")
    
    elif generate_plan and not selected_meals:
        st.error("Please select at least one meal before generating the plan!")

if __name__ == "__main__":
    main()