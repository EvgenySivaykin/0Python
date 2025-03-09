# api_key = 'sk-1234567890abcdef1234567890abcdef'

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

# client = OpenAIClient(api_key)
print(api_key)