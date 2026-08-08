from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Hi! My name is Pavan. Please remember it."
)
print(response.text)

'''
output - its promised I will remember it.
Hi Pavan! It is great to meet you. I have noted your name and will definitely remember it. 

How can I help you today?
'''

#Next time ask again
# when you calling LLM using generate_content it doesnt store previous conversations.
# It doesnt have memory
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="what is my name?"
)
print(response.text)

#Using the List we can add the memory or context 
conversation_history = []

def chat(user_message):
    # 1. add what the user said to memory
    conversation_history.append({"role": "user", "parts": [{"text": user_message}]})

    # 2. send the ENTIRE conversation history to the LLM
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=conversation_history
        )
        reply = response.text
    except Exception as e:
        return f"Sorry, something went wrong: {e}"

    #3. add the AI's reply to memory too, so it remembers the conversation next time
    conversation_history.append({"role": "model", "parts": [{"text": reply}]})
    return reply

print(chat("Hi! My name is Pavan. Please remember it."))
print(chat("what is my name?"))

#print conversation_history
print(conversation_history)
for msg in conversation_history:
    print(msg)
