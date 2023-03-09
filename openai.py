import openai, os
from dotenv import load_dotenv
load_dotenv()

async def get_chatgpt_text(content):
  openai.api_key = os.environ.get('Openai-Api-Token')

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature = 2,
    messages=[
      {"role": "user", "content": content}
    ]
  )
  return completion.choices[0].message.content
  