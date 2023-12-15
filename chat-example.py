import random

# Define a dictionary of responses to different user inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks for asking!", "I'm good, how about you?", "I'm great, thanks!"],
    "what's your name": ["My name is Bot.", "I'm Bot, nice to meet you!", "You can call me Bot."],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"]
}

# Define a function to generate a response to user input
def generate_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()

    # Check if the user input is in the dictionary of responses
    if user_input in responses:
        # Choose a random response from the list of responses for the user input
        response = random.choice(responses[user_input])
    else:
        # If the user input is not in the dictionary of responses, choose a default response
        response = "I'm sorry, I didn't understand what you said. Can you please say that again?"

    return response

# Define a loop to get user input and generate responses
while True:
    # Get user input
    user_input = input("You: ")

    # Generate a response to the user input
    response = generate_response(user_input)

    # Print the response
    print("Bot:", response)

