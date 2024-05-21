from dotenv import load_dotenv

from openai import OpenAI
import instructor

from schema.config import GptModel
from schema.texts import Client_Model_1

load_dotenv()
client = instructor.patch(OpenAI())

class ChatClient:
    def __init__(self, model:GptModel, response_model):
        self.model = model
        self.response_model = response_model

    def chat_completion(self, user_message:str):
        return client.chat.completions.create(
            model=self.model,
            response_model=self.response_model,
            messages= [
                {"role":"user", "content": user_message}
                ]
            )

chat_client = ChatClient(model=GptModel.GPT_3, response_model= Client_Model_1)

