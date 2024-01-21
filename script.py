from dotenv import load_dotenv
import os, pickle, asyncio
load_dotenv(".env")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
from openai import OpenAI
client = OpenAI(api_key=OPENAI_KEY)

file = open("instructions.txt", "r")
instructions = file.read()
file = open("test.txt", "r")
abstracts = file.read()

def get_category (instructions, abstracts):

   response = client.chat.completions.create(
   model="gpt-3.5-turbo-1106",
   temperature=1,
  # response_format={ "type": "json_object" },
   messages=[
        {"role": "system", "content": "You are a useful assistant"},
        {"role": "user", "content": abstracts}
    ]
   )
   return response.choices[0].message.content

with open("output.txt", "w") as file:
	content = get_category (instructions, abstracts)
	file.write(content)
	file.close()