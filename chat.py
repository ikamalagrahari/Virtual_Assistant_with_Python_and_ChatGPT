import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to generate a response to user input
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Define a loop to get user input and generate responses
while True:
    # Get user input
    user_input = input("You: ")

    # Generate a response to the user input
    response = generate_response(f"User: {user_input}\nBot:")

    # Print the response
    print(response)

