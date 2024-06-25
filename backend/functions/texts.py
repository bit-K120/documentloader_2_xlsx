import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '..')))

from config import chat_client
from functions.prompts import user_message

response = chat_client.chat_completion(user_message)
print(response)

