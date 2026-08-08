conversation_history = []

def chat(user_message):
    # This is a simple chat function that takes a user message and returns a response
    return f"Bot: I received your message: {user_message}"

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
        return f"Error: {e}"

    #3. add the AI's reply to memory too, so it remembers the conversation next time
    conversation_history.append({"role": "model", "parts": [{"text": reply}]})
    return reply


