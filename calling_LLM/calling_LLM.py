from pydantic import BaseModel
from dotenv import load_dotenv

#calling LLM Model programatically using Google Gemini API

#here we are calling the Google gemini model to interact with the LLM
#Google Gemini API is a powerful tool that allows developers to integrate 
# advanced language models into their applications. 
# It provides a simple and efficient way to generate human-like text, answer questions,
#  and perform various natural language processing tasks.
#URL : https://ai.google.dev/gemini-api/docs/models

#Install the SDK using pip
#pip install -U google-genai

#Initialize the Gemini API client
from google import genai
load_dotenv()  # Load the key into an environment variables from .env file

#Client is class that provides methods to interact with the Google Gemini API.
client = genai.Client()

#Generate content using the Gemini API
#Models are pre-trained language models that can generate text based on the input provided.
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Tell me who invented Samosa in 3 lines?"
)
print(response.text)

'''
The samosa was not invented by a single person but originated in the medieval Middle East as a savory pastry called *sanbosag*. 
Middle Eastern merchants and Central Asian traders introduced it to the Indian subcontinent during the Delhi Sultanate in the 13th century. 
It was first famously documented in India as a royal delicacy by the poet Amir Khusrau and the traveler Ibn Battuta.
'''

#setup the API key for authentication
#To use the Google Gemini API, you need to set up an API key for authentication.
#To set up the API key, you can use the dotenv library to load it from a .env file:
#from Google AI Studio , you can get the API key.

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
    
    # Call the Google Gemini API to generate content
    # when you calling LLM using generate_content it doesnt store previous conversations.
    # It doesnt have memory
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    return response.text

recipe = generate_recipe(["dal", "rice", "tomatoes", "onions", "salt", "lentils"], "Indian", "vegetarian")
print("Generated Recipe:\n", recipe)

#output:
'''
It was introduced to the Indian subcontinent around the 13th century by Central Asian merchants and chefs during the Delhi Sultanate. 
Over the centuries, Indian cooks adapted the recipe, replacing the original meat filling with the spiced potato mixture popular today.
Generated Recipe:
 **Indian Tomato Lentil Khichdi**

Combine 1/2 cup rice, 1/4 cup dal, and 1/4 cup lentils; wash thoroughly. In a pot, sauté one chopped onion and two diced tomatoes until soft. Stir in the rinsed rice, dal, lentils, four cups of water, and salt to taste. Bring to a boil, then cover and simmer on low heat for 20 minutes until the grains are mushy and fully cooked. Stir well and serve this comforting, warm vegetarian meal immediately.
'''

recipe = generate_recipe(["Corn", "Black beans", "Avacoda"], "Mexican", "Vegan")
print("Generated Recipe:\n", recipe)    