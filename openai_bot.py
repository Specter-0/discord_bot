import openai


ere = "jfuie fwucdhc9uwhefiud u fhdsiuf hsdiy  fhudsif biya  cduahf iyab fadhc hbyifcsd bxyfic gbeqxasyixz h bfyadixzbc8yiqw"
print(print(len(ere), "\n", ere[:75]))

def get_chatgpt_text(content):
  openai.api_key = "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"

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature = 2,
    messages=[
      {"role": "user", "content": content}
    ]
  )
  return completion.choices[0].message.content
  