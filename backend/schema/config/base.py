from enum import Enum
from pydantic import BaseModel, EmailStr
from schema.texts import (
    Client_Model_1
    )


class GptModel(str, Enum):
    GPT_3 = "gpt-3.5-turbo"
    GPT_4o = "gpt-4o"

class ResponseModel(Enum):
    MODEL_1 = Client_Model_1




