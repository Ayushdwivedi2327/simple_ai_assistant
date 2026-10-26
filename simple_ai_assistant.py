from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(
   base_url=os.getenv("base_url"),
   api_key=os.getenv("api_key")
)

while True:
    user_inp = input("You :\n")
    if user_inp.lower() in ["exit","bye","quit","goodbye"]:
        break
    response = client.chat.completions.create(
    model=os.getenv("model"),
    messages=[ 
        {"role": "user", "content": user_inp}
    ]
)
    print("Assistant : " , response.choices[0].message.content)