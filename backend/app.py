from config import chat_client
from functions.xlsx import WriteExcel
from functions.prompts import user_message

format_data = chat_client.chat_completion(user_message)
ws = WriteExcel(format_data)
ws.export_to_xlsx()

