from dotenv import load_dotenv
from google.genai import types
from pydantic import BaseModel
from google import genai

# Structured Output from LLM
#By using pydantic models

load_dotenv()
client = genai.Client()

class Recipe(BaseModel):
    title: str
    ingredients: list[str]
    calories: int
    prep_time_minutes: int

#call the Gemini LLM
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Generate a recipe for Indian dal recipe.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json", #reply in JSON
        response_schema=Recipe  #..in exactly this shape
    )
)
print(response.text)

recipe =response.parsed
print(recipe)
print(recipe.calories)