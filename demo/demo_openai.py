import os
import openai
openai.organization = os.getenv("OPENAI_ORGANISATION_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
import json

# get list of all models
with open("open-ai-models.json","w") as fp:
    json.dump(openai.Model.list(), fp)


