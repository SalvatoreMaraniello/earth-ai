import os
import openai
openai.organization = os.getenv("OPENAI_ORGANISATION_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
import json


path_or_url =  "./images/28-northampton-rd-croydon-wider.png"

model_id = "gpt-4-0613"

# completion = openai.Image.create_variation(
#   image=open(path_or_url, "rb"),
#   messages=[
#     # {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Can you highlight the windows in this image? Can you tell me the size?"}
#   ]
#   n=2,
#   size="1024x1024"
# )

res = openai.Image.create_edit(
  image=open(path_or_url, "rb"),
  prompt="Delete the windows and replace them with a red box. Do not change the aspect ratio of the picture.",
  n=4,
  size="1024x1024"
)
for url in res["data"]:
    print(url)



