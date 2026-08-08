from pydantic import BaseModel

#calling LLM
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

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    prompt="Tell me who invented Samosa in 3 lines?",
    max_output_tokens=100
)

print(response.output_text)

#setup the API key for authentication
#To use the Google Gemini API, you need to set up an API key for authentication.
#To set up the API key, you can use the dotenv library to load it from a .env file: