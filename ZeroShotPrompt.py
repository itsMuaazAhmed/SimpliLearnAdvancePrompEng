import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())  # read local .env file
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is missing. Create a .env file with OPENAI_API_KEY=your_key or export it in your terminal."
    )

client = OpenAI(api_key=api_key)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content


prompt = """
translate this to german:
'You are a helpful assistant today.'
"""

response = get_completion(prompt)
print(response)