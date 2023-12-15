import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt you want to generate a response for
prompt = "Hello, what's your name?"

# Use the OpenAI API to generate a response to the prompt
response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=0.5,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Print the generated response
print(response.choices[0].text.strip())

