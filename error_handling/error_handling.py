#Throwing exception
'''
revenue=0
expenses=10
profit=revenue-expenses
margin=profit * 100/revenue
print(margin)

#output- ZeroDivisionError: division by zero
'''

#Handling the exception - by catching them..program will not crash
from dotenv import load_dotenv
from google import genai
load_dotenv()

revenue=0
expenses=10
profit=revenue-expenses
try:
    margin=profit * 100/revenue
    print(f"Margin: {margin:.2f}%")
except ZeroDivisionError:
    print("Error: Revenue is 0, cannot calculate margin. Skipping...")

def safe_margin(revenue, expenses):
    profit = revenue - expenses
    try:
        margin = profit * 100 / revenue
        return f"Margin: {margin:.2f}%"
    except ZeroDivisionError: 
        return None #signal could not calculate margin

print(safe_margin(0, 10))
print(safe_margin(100, 10))

#Grab the error object with 'as e' to see the message
try:
    age=int(input("Enter your age: "))
except ValueError as e:
    print("could not convert input to number")
    print(f"Error: {e}")

#output
"""
Enter your age: twenty
could not convert input to number
Error: invalid literal for int() with base 10: 'twenty'
"""

# Define a client for the recipe generation API.
client = genai.Client()

def generate_recipe(ingredients, cuisine, diet):
    """
    Generate a recipe using ingredients provided.
    
    Cuisine can be Indian, Mexican, Italian, etc.
    diet can be vegetarian, vegan, gluten-free, etc.
    ingredients can be a list of ingredients like ["dal", "rice", "tomatoes"]
    """

    # Create a prompt for the LLM
    prompt = f'''
    Generate one food recipe using the following ingredients: {', '.join(ingredients)}.
    Recipe should not be more than 100 words.
    Cuisine: {cuisine}
    Dietary Restrictions: {diet}
    '''
    try:
        # Call the Google Gemini API to generate content
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        # Check if the model returned an empty response..
        if not response.text:
            return "The model returned an empty response. Please try again."
        return response.text
    except Exception as e:
        print(f"Error generating recipe: {e}")
        return f"Failed to generate recipe. Error: {e}"

recipe = generate_recipe(["dal", "rice", "tomatoes", "onions", "salt", "lentils"], "Indian", "vegetarian")
print("Generated Recipe:\n", recipe)

#output
'''
ValueError: No API key was provided. Please pass a valid API key. Learn how to create an API key at https://ai.google.dev/gemini-api/docs/api-key.
'''
