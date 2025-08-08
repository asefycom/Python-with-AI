# Install "together" and "python_dotenv" packages first
# pip istall at your system or !pip install at your jupyter notebook
import os
from together import Together
from dotenv import load_dotenv

# Get the OpenAI API key from the .env file
load_dotenv('.env', override=True)
together_api_key = os.getenv('TOGETHER_API_KEY')

# Set up the Together client
client = Together(api_key=together_api_key)


def print_llm_response(prompt):
    response = client.chat.completions.create(
        model="google/gemma-3n-E4B-it",
        # model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
        {
            "role": "user",
            "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32 
    return fahrenheit
