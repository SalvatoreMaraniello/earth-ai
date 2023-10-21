import os
import openai
from PIL import Image, ImageDraw

openai.organization = os.getenv("OPENAI_ORGANISATION_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
import json

path_or_url =  "./images/28-northampton-rd-croydon-wider.png"

res = openai.Image.create_edit(
  image=open(path_or_url, "rb"),
  prompt="Delete the windows and replace them with a red box. Do not change the aspect ratio of the picture.",
  n=4,
  size="1024x1024"
)
for url in res["data"]:
    print(url)

