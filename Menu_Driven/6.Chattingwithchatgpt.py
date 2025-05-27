import openai

def get_api_key():
    return 'your api key'  # Replace with your actual API key

def get_chatgpt_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None

def chat_with_gpt():
    openai.api_key = get_api_key()

    # Initial system message to set up the assistant's behavior
    conversation = [
        {"role": "system", "content": "You are a friendly and knowledgeable assistant."}
    ]

    print("ChatGPT: Hello! How can I assist you today? (type 'exit' to stop)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatGPT: Goodbye! Have a great day.")
            break

        conversation.append({"role": "user", "content": user_input})
        response = get_chatgpt_response(conversation)

        if response:
            print(f"ChatGPT: {response}")
            conversation.append({"role": "assistant", "content": response})
        else:
            print("ChatGPT: Oops, something went wrong. Please try again.")