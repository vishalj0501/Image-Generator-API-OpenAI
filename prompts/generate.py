import os
import sys
import openai
import json
from dotenv import load_dotenv
from model.model import Description
from fastapi.response import Response

load_dotenv()
# sys.path.append(sys)
# print("-----\n")
# print(sys.path[0])

sys.path.append(sys.path.append(sys.path[0] + "/.."))

class ImageGenerator:
    def __init__(self):
        openai.api_key = os.getenv("API_KEY")
        self.APIKey=openai.api_key

    def generateImage(self, description: Description):
        prompt = description.prompt
        n = description.n
        squareSize = description.squareSize
        # response = openai.Completion.create(
        #     engine="davinci",
        #     prompt=prompt,
        #     temperature=0.9,
        #     max_tokens=100,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0.6,
        #     stop=["\n", " Image:"],
        # )
        # return response.choices[0].text


