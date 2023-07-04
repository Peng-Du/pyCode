import os
import openai
import webbrowser

openai.api_key = os.environ.get('OPENAI_API_KEY')

response = openai.Image.create(
  prompt="a bird in an apple tree",
  n=1,
  size="1024x1024"
)

print(response)

image_url = response['data'][0]['url']

webbrowser.open(image_url)