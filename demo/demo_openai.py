import os
import openai
openai.organization = os.getenv("OPENAI_ORGANISATION_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
import json

# get list of all models
with open("open-ai-models.json","w") as fp:
    json.dump(openai.Model.list(), fp)

### list available models.
# for m in openai.Model.list()["data"]:
#     print(m["id"])

# get gpt-4 model
# m = openai.Model(id="gpt-4-0613")


model_id = "gpt-4-0613"


## chat completion
completion = openai.ChatCompletion.create(
  model=model_id,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)
print(completion.choices[0].message)


openai.Image.create_variation(
  image=open("otter.png", "rb"),
  n=2,
  size="1024x1024"
)