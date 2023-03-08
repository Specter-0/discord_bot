import openai, os
from dotenv import load_dotenv
load_dotenv()


ere = "jfuie fwucdhc9uwhefiud u fhdsiuf hsdiy  fhudsif biya  cduahf iyab fadhc hbyifcsd bxyfic gbeqxasyixz h bfyadixzbc8yiqw"
print(print(len(ere), "\n", ere[:75]))

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
  