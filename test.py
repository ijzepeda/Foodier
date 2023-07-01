import json

# Define a mapping to extract data from the source JSON to your own JSON
mapping = {
    "day": "Day",
    "breakfast": "Breakfast",
    "lunch": "Lunch",
    "dinner": "Dinner",
}

# Your source JSON
source_json_str = '''
{
  "meal_plan": [
    {
      "day": "Monday",
      "breakfast": "Oatmeal with fruit",
      "lunch": "Grilled portobello mushroom sandwiches",
      "dinner": "Spaghetti with marinara sauce and roasted vegetables"
    },
    {
      "day": "Tuesday",
      "breakfast": "Scrambled tofu with vegetables",
      "lunch": "Black bean and corn salad with avocado dressing",
      "dinner": "Spicy peanut sauce with rice and vegetables"
    },
    {
      "day": "Wednesday",
      "breakfast": "Blueberry smoothie",
      "lunch": "Garlic herb roasted potatoes with salad",
      "dinner": "Vegetable stir fry with tofu and brown rice"
    },
    {
      "day": "Thursday",
      "breakfast": "Pancakes with maple syrup and fruit",
      "lunch": "Hummus wrap with hummus, a handful of spinach, tomato and cucumber in a large whole wheat tortilla",
      "dinner": "Roasted cauliflower and chickpea burritos"
    },
    {
      "day": "Friday",
      "breakfast": "cereal with milk",
      "lunch": "Lentil soup",
      "dinner": "Quinoa and black bean stuffed sweet potatoes"
    },
    {
      "day": "Saturday",
      "breakfast": "avocado toast",
      "lunch": "Spinach and fruit smoothies",
      "dinner": "roasted vegetables and hummus wrap"
    },
    {
      "day": "Sunday",
      "breakfast": "Tofu scramble",
      "lunch": "avocado toast",
      "dinner": "Spaghetti with marinara sauce and roasted vegetables"
    }
  ]
}
'''
from models.json_struct import base_structure
# Load source JSON string into a Python dictionary
# source_json = json.loads(source_json_str)
source_json = base_structure
# Initialize your own JSON structure
your_json = {"Days": []}

# Extract data from the source JSON and fill your own JSON structure
for meal_data in source_json["meal_plan"]:
    day_data = {}
    for source_key, target_key in mapping.items():
        day_data[target_key] = meal_data[source_key]
    your_json["Days"].append(day_data)

# Convert your JSON to a string
your_json_str = json.dumps(your_json, indent=2)

# Print your JSON
print(your_json_str)







def ap2():
    from models.json_struct import base_structure

    def has_specific_structure(json_data):
        # Define the expected structure
        expected_structure = base_structure
        # Check if the JSON structure matches the expected structure
        try:
            for day, meals in json_data.items():
                if day not in expected_structure:
                    return False
                for meal, meal_data in meals.items():
                    if meal not in expected_structure[day]:
                        return False
                    for key, value_type in expected_structure[day][meal].items():
                        if not isinstance(meal_data.get(key), value_type):
                            return False
        except AttributeError:
            return False

        return True
