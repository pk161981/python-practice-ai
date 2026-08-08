from dotenv import load_dotenv
from google import genai

# Recipe Generator App - uses Google Gemini API to generate a recipe
# based on ingredients, cuisine, and dietary restrictions provided by the user.

load_dotenv()  # Load the API key from .env file into environment variables

client = genai.Client()

MODEL = "gemini-3.5-flash"


def generate_recipe(ingredients, cuisine, diet):
    """
    Generate a recipe using the given ingredients, cuisine, and diet.

    ingredients: list of ingredients, e.g. ["dal", "rice", "tomatoes"]
    cuisine: e.g. "Indian", "Mexican", "Italian"
    diet: e.g. "vegetarian", "vegan", "gluten-free"
    """
    prompt = f'''
    Generate one food recipe using the following ingredients: {', '.join(ingredients)}.
    Recipe should not be more than 150 words.
    Include a recipe title, list of ingredients with quantities, and preparation steps.
    Cuisine: {cuisine}
    Dietary Restrictions: {diet}
    '''

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text


def get_ingredients_from_user():
    raw = input("Enter ingredients (comma separated): ").strip()
    ingredients = [item.strip() for item in raw.split(",") if item.strip()]
    while not ingredients:
        raw = input("Please enter at least one ingredient: ").strip()
        ingredients = [item.strip() for item in raw.split(",") if item.strip()]
    return ingredients


def main():
    print("=== AI Recipe Generator ===\n")

    ingredients = get_ingredients_from_user()
    cuisine = input("Enter cuisine (e.g. Indian, Mexican, Italian) [Any]: ").strip() or "Any"
    diet = input("Enter dietary restriction (e.g. vegetarian, vegan, gluten-free) [None]: ").strip() or "None"

    print("\nGenerating your recipe...\n")
    recipe = generate_recipe(ingredients, cuisine, diet)

    print("=== Generated Recipe ===\n")
    print(recipe)

    while True:
        again = input("\nGenerate another recipe? (y/n): ").strip().lower()
        if again != "y":
            break
        ingredients = get_ingredients_from_user()
        cuisine = input("Enter cuisine (e.g. Indian, Mexican, Italian) [Any]: ").strip() or "Any"
        diet = input("Enter dietary restriction (e.g. vegetarian, vegan, gluten-free) [None]: ").strip() or "None"
        print("\nGenerating your recipe...\n")
        recipe = generate_recipe(ingredients, cuisine, diet)
        print("=== Generated Recipe ===\n")
        print(recipe)


if __name__ == "__main__":
    main()
