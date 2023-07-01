# TODO:
# TODO: parse different jsons 
# TODO: send email with ingredients
# TODO: 
# TODO: adapt summarizer for Q&A
# TODO: 





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





import cohere
co = cohere.Client('dOsQbNVpPcIncdDvTBecyzdK1a7zupSgYJghCqV3') # This is your trial API key
response = co.generate(
  model='command',
  prompt='Create a weekly meal plan for 3 meals per day, for a 30 years man, with 165 cm and 65 kg, with 2000 calories daily, on a 100 dollars budget. Make all meals Vegan, and Avoid these ingredients: peanuts. And create a list of all ingredients.\nStructure the text in JSON format, including the name of the day, the name of the dish, and all ingredients together unsorted at the end\nDo not include extra text or descriptions. Provide different dishes on different days\nUse this JSON Structure:\n{\n  Monday: {\n    Breakfast: str,\n    Lunch: str,\n    Dinner: str\n  },\n# repeat for all 5 days\nIngredients: list\n}',
  max_tokens=3058,
  temperature=0.5,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))