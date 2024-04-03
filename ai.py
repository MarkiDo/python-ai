import os
import re
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

api_key = os.environ.get('API_KEY')

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

client = OpenAI(api_key=api_key)

def comp(PROMPT, MaxToken=50):
    pattern = r'[!@#$%^&*(),.?":{}|<>]'
    if not re.search(pattern,PROMPT):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": PROMPT }],
            max_tokens=MaxToken,
            temperature=0
        )
        return print(GREEN+response.choices[0].message.content+RESET)
    else:
        return print(RED + 'Incorrect input'+ RESET)

PROMPT = input('Ask ChatGPT a question: ')

comp(PROMPT, MaxToken=3000)
