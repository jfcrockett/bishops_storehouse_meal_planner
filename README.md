# Bishop's Storehouse Meal Planner

A Streamlit application that helps users create two-week meal plans using ingredients available at the Bishop's Storehouse. The app generates a shopping list with exact quantities needed and provides simple recipe instructions for each meal.

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
