import openai
import argparse
import logging
from decouple import config

# Read the OpenAI API key from the .env file
api_key = config('OPENAI_API_KEY')

openai.api_key = api_key

# Configure logging
logging.basicConfig(filename="chatgpt_debug.log", level=logging.DEBUG, format="%(asctime)s [%(levelname)s]: %(message)s")

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message["content"]
        return reply
    except Exception as e:
        logging.error(f"Error in chat_with_gpt: {e}")
        return "An error occurred. Check the logs for details."

def main():
    parser = argparse.ArgumentParser(description="Chat with GPT-3 via the terminal.")
    parser.add_argument("--query", type=str, help="Input your query to GPT-3.")
    
    args = parser.parse_args()
    
    while True:
        if args.query:
            user_input = args.query
            args.query = None  # Reset the query argument to None
        else:
            user_input = input("You: ")
            logging.info(f"You: {user_input}")

        if user_input.lower() == "--logchat":
            break  # Exit the conversation if the special command is submitted

        response = chat_with_gpt(user_input, model="gpt-3.5-turbo")  # Use the "gpt-3.5-turbo" model
        print(f"AI: {response}")
        logging.info(f"AI: {response}")

if __name__ == "__main__":
    main()
