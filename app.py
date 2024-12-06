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
        'Oatmeal with Honey and Fruit': {
            'ingredients': {
                'rolled oats': 1/12,
                'honey': 1/24,
                'milk': 1/16
            },
            'instructions': [
                "Bring milk to a gentle boil",
                "Add oats and reduce heat to medium-low",
                "Cook for 5 minutes, stirring occasionally",
                "Remove from heat and let stand for 2 minutes",
                "Top with honey"
            ]
        },
        'Pancakes with Syrup': {
            'ingredients': {
                'pancake mix': 1/24,
                'eggs': 1/4,
                'milk': 1/16
            },
            'instructions': [
                "Mix pancake mix, eggs, and milk in a bowl until just combined (small lumps are okay)",
                "Heat a pan or griddle over medium heat",
                "Pour about 1/4 cup batter for each pancake",
                "Cook until bubbles form on surface, then flip",
                "Cook other side until golden brown"
            ]
        },
        'Apple Cinnamon Oatmeal': {
            'ingredients': {
                'rolled oats': 1/12,
                'applesauce': 1/6,
                'cinnamon': 1/24,
                'milk': 1/16
            },
            'instructions': [
                "Heat milk in a pan until warm",
                "Add oats and cook on medium-low heat",
                "Stir in applesauce and cinnamon",
                "Cook until desired consistency",
                "Add more milk if needed"
            ]
        },
'Breakfast Rice Pudding': {
            'ingredients': {
                'rice': 1/12,
                'milk': 1/16,
                'cinnamon': 1/24,
                'raisins': 1/24
            },
            'instructions': [
                "Heat cooked rice with milk",
                "Add cinnamon and raisins",
                "Cook until creamy, stirring often",
                "Let stand 5 minutes before serving"
            ]
        },
        'PB Banana Oatmeal': {
            'ingredients': {
                'rolled oats': 1/12,
                'peanut butter': 1/24,
                'milk': 1/16
            },
            'instructions': [
                "Cook oats with milk according to package directions",
                "Stir in peanut butter until melted",
                "Top with additional peanut butter if desired"
            ]
        },
        'Cereal Parfait': {
            'ingredients': {
                'honey nut o\'s': 1/8,
                'applesauce': 1/6,
                'vanilla yogurt': 1/8
            },
            'instructions': [
                "Layer vanilla yogurt in a bowl",
                "Add a layer of applesauce",
                "Top with crushed cereal",
                "Repeat layers if desired"
            ]
        }
    },
    'Lunch': {
        'Tuna Sandwich': {
            'ingredients': {
                'tuna': 1/2,
                'bread': 2/10,
                'mayo': 1/24
            },
            'instructions': [
                "Drain tuna well",
                "Mix tuna with mayo in a bowl",
                "Spread on bread slices",
                "Optional: add any available vegetables"
            ]
        },
        'Black Bean Soup': {
            'ingredients': {
                'black beans': 1/3,
                'diced tomatoes': 1/4,
                'rice': 1/12
            },
            'instructions': [
                "Heat black beans with their liquid",
                "Add diced tomatoes",
                "Serve over cooked rice",
                "Optional: top with any available fresh vegetables"
            ]
        },
        'Rice and Egg Bowl': {
            'ingredients': {
                'rice': 1/12,
                'eggs': 1/4
            },
            'instructions': [
                "Cook rice according to package directions",
                "Scramble eggs in a pan",
                "Serve eggs over rice"
            ]
        },
        'Three Bean Salad': {
            'ingredients': {
                'black beans': 1/3,
                'white beans': 1/3,
                'green beans': 1/3
            },
            'instructions': [
                "Drain and rinse beans",
                "Mix all beans together",
                "Season with any available seasonings",
                "Best if chilled before serving"
            ]
        },
        'Chicken Rice Soup': {
            'ingredients': {
                'chicken rotini soup': 1/2,
                'rice': 1/12
            },
            'instructions': [
                "Heat soup in a pan",
                "Add cooked rice",
                "Simmer for 5 minutes",
                "Let stand briefly before serving"
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
                "Bring a large pot of water to boil",
                "Add spaghetti and cook according to package directions",
                "Meanwhile, heat the fully cooked beef in a pan",
                "Add spaghetti sauce to beef and heat through",
                "Drain pasta and top with meat sauce"
            ]
        },
        'Mexican Rice Bowl': {
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
                "Layer rice, beans, and corn in bowls",
                "Top with salsa and cheese"
            ]
        },
        'Chicken and Dumplings Soup': {
            'ingredients': {
                'cream of chicken soup': 1/2,
                'chicken breast pieces': 1/2,
                'pancake mix': 1/24
            },
            'instructions': [
                "Heat soup and chicken in a pot",
                "Mix pancake mix with water to make dumpling dough",
                "Drop small spoonfuls of dough into simmering soup",
                "Cover and cook 15 minutes"
            ]
        },
        'Bean and Cheese Enchiladas': {
            'ingredients': {
                'refried beans': 1/6,
                'tortillas': 2/6,
                'cheddar cheese': 1/8,
                'diced tomatoes': 1/4
            },
            'instructions': [
                "Spread beans on tortillas",
                "Add cheese and roll up",
                "Top with warm diced tomatoes",
                "Heat until cheese melts"
            ]
        },
        'Beef and Bean Burritos': {
            'ingredients': {
                'fully cooked beef': 1/2,
                'refried beans': 1/6,
                'tortillas': 2/6,
                'salsa': 1/8
            },
            'instructions': [
                "Heat beef and beans separately",
                "Warm tortillas",
                "Fill tortillas with beef and beans",
                "Top with salsa and roll up"
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