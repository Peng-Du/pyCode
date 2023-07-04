import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "Where is Burkina Faso?"}]
)

print(completion)