import sys
import os

from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import instructor
from functions.prompts import system_message, user_message



load_dotenv()
cwd = os.getcwd()
project_root = os.path.dirname(cwd)

if project_root not in sys.path:
    sys.path.append(cwd)

client = instructor.patch(OpenAI())


class ClientDetail(BaseModel):
    name:str
    age:int

completion:ClientDetail = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=ClientDetail,
    messages = [
        {"role":"user", "content":user_message}
        ]
    )

print(completion)

