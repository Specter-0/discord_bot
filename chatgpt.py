import openai, os
from dotenv import load_dotenv
load_dotenv()

async def get_chatgpt_text(content):
  openai.api_key = os.environ.get('Openai-Api-Token') # api key via .env file

  completion = openai.ChatCompletion.create( # sends a message to gpt and waits for ansawer
    model="gpt-3.5-turbo",
    temperature = 2, # how different each mesasge will be
    messages=[
      {"role": "user", "content": content} # message to gpt
    ]
  )
  return completion.choices[0].message.content
  