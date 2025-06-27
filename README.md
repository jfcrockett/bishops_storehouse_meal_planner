# Bishop's Storehouse Meal Planner

A Streamlit app that helps create two-week meal plans using ingredients available at the Bishop's Storehouse.

## Files Overview

### Core Application
- `app.py` - Main Streamlit application

### Data Files (Easy to Edit!)
- `ingredients.txt` - All available ingredients with package sizes and serving information
- `meal_options.txt` - All meal recipes organized by breakfast, lunch, and dinner

## Data File Formats

### ingredients.txt Format
```
# Comments start with # and are ignored
ingredient_name | package_size | servings_per_package | unit

# Example:
tuna | 5 | 2 | oz
bread | 20 | 10 | slices
eggs | 12 | 4 | count
```

### meal_options.txt Format
```
[MEAL_TYPE]

Meal Name
ingredient1 | portion_needed
ingredient2 | portion_needed
INSTRUCTIONS:
1. First step
2. Second step

# Example:
[BREAKFAST]

Scrambled Eggs & Toast
eggs | 0.25
butter | 0.031
bread | 0.2
cheddar cheese | 0.125
INSTRUCTIONS:
1. Beat eggs in a bowl
2. Heat butter in a pan over low heat
3. Add eggs and scramble gently until set
4. Toast bread slices
5. Serve eggs over toast, topped with cheese
```

## How to Edit

### Adding New Ingredients
1. Open `ingredients.txt`
2. Add a new line with: `ingredient_name | package_size | servings_per_package | unit`
3. Save the file

### Adding New Meals
1. Open `meal_options.txt`
2. Find the appropriate section: `[BREAKFAST]`, `[LUNCH]`, or `[DINNER]`
3. Add your meal following the format above
4. Portion numbers are decimals (e.g., 0.5 = half of a package's servings)
5. Save the file

### Editing Existing Meals
1. Open `meal_options.txt`
2. Find the meal you want to edit
3. Modify ingredients, portions, or instructions
4. Save the file

### Understanding Portions
- Portions are fractions of the package's total servings
- Example: If rice has 12 servings per package and you need 1 serving, use `0.083` (1/12)
- Example: If you need half a can of tuna (1 out of 2 servings), use `0.5`

## Running the App

```bash
streamlit run app.py
```

## Features

- ✅ Select preferred meals from each category
- ✅ Generate 14-day meal plan for your family size
- ✅ Get shopping list with practical measurements
- ✅ View recipes scaled for your family
- ✅ Download printable meal plan
- ✅ Easy-to-edit data files

## Benefits of Separate Data Files

1. **Easy Editing** - No need to understand Python code
2. **Quick Updates** - Change ingredients or recipes instantly
3. **Collaboration** - Multiple people can edit different files
4. **Version Control** - Track changes to ingredients and recipes separately
5. **Backup** - Easy to backup just the data files
6. **Customization** - Adapt for different regions or dietary needs

## File Structure
```
bishops_storehouse_meal_planner/
├── app.py              # Main application
├── ingredients.txt     # Ingredient database
├── meal_options.txt    # Recipe database
└── README.md          # This file
```

## Notes

- The app automatically loads data from the text files when it starts
- If a file is missing or has errors, the app will show an error message
- Always use the pipe character `|` as the separator in data files
- Decimal portions should use dots (.) not commas
- Comment lines start with `#` and are ignored

## Features

- Create two-week meal plans for households of any size
- Choose from multiple breakfast, lunch, and dinner options
- View simple recipe instructions for each meal
- Get an accurate shopping list based on package sizes available
- See ingredient quantities needed for your household size
- All recipes use ingredients available at Bishop's Storehouse

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/bishops-storehouse-meal-planning.git
cd bishops-storehouse-meal-planning
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install streamlit
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. In your web browser:
- Enter the number of people in your household
- Select your preferred meals from each category
- Click "Generate Meal Plan" to create your two-week plan
- View recipes and shopping list
- Each recipe includes step-by-step instructions

## Application Structure

- `app.py`: Main application file containing all code
- Key components:
  - `MEAL_PORTIONS`: Dictionary of available ingredients and their portion sizes
  - `MEALS`: Dictionary of all recipes with ingredients and instructions
  - Calculate functions for determining required quantities
  - Streamlit interface for user interaction

## How It Works

1. **Meal Selection**: Users choose from available breakfast, lunch, and dinner options
2. **Portion Calculation**: The app calculates precise portions based on:
   - Number of people in the household
   - Package sizes available at Bishop's Storehouse
   - Standard serving sizes
3. **Shopping List Generation**: Creates a list of required items with exact quantities
4. **Recipe Display**: Shows simple, step-by-step instructions for each meal

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Some ways to contribute:
- Add new recipes using available ingredients
- Improve portion calculations
- Enhance the user interface
- Add new features
- Fix bugs

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors who have helped with recipes and portion calculations
- Bishop's Storehouse for providing the ingredient list and package sizes

## Support

For issues, questions, or contributions, please:
1. Open an issue in the GitHub repository
2. Submit a pull request with your improvements
3. Contact the maintainer

## Future Enhancements

- Add nutritional information for meals
- Include meal prep instructions
- Add dietary restriction filters
- Implement meal favorites
- Add seasonal recipe variations
