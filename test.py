import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)

print(completion.data[0].url)