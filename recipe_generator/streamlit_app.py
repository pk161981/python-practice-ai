import streamlit as st
from dotenv import load_dotenv
from google import genai

# Streamlit Recipe Generator App - uses Google Gemini API to generate a recipe
# based on ingredients, cuisine, and dietary restrictions provided by the user.

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.5-flash"

def generate_recipe(ingredients, cuisine, diet):
    prompt = f'''
    Generate one food recipe using the following ingredients: {', '.join(ingredients)}.
    Recipe should not be more than 150 words.
    Include a recipe title, list of ingredients with quantities, and preparation steps.
    Cuisine: {cuisine}
    Dietary Restrictions: {diet}
    '''

    #call the Google Gemini API to generate content
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text


st.set_page_config(page_title="AI Recipe Generator", page_icon="🍲")
st.title("🍲 AI Recipe Generator11")
st.write("Enter your ingredients and preferences, and let AI create a recipe for you.")

with st.form("recipe_form"):
    ingredients_raw = st.text_input("Ingredients (comma separated)", placeholder="e.g. rice, dal, tomatoes, onions")
    cuisine = st.text_input("Cuisine", placeholder="e.g. Indian, Mexican, Italian", value="Any")
    diet = st.text_input("Dietary Restrictions", placeholder="e.g. vegetarian, vegan, gluten-free", value="None")
    submitted = st.form_submit_button("Generate Recipe")

if submitted:
    ingredients = [
        item.strip() for item in ingredients_raw.split(",") if item.strip()
    ]
    # ingredients = []
    # for item in ingredients_raw.split(","):
    #     item = item.strip()
    #     if item:
    #         ingredients.append(item)
    if not ingredients:
        st.error("Please enter at least one ingredient.")
    else:
        with st.spinner("Generating your recipe..."):
            recipe = generate_recipe(ingredients, cuisine or "Any", diet or "None")
        st.subheader("Generated Recipe")
        st.markdown(recipe)
