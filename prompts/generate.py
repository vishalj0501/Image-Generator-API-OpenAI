import os
import sys
import openai
import json
from dotenv import load_dotenv
# import models
from models.model import Description
# from fastapi.response import Response
# from dataclasses import dataclass

load_dotenv()
# sys.path.append(sys)
# print("-----\n")
# print(sys.path[0])




sys.path.append(sys.path.append(sys.path[0] + "/.."))
# @dataclass
# class Description():
#     def __init__(self, prompt, n, squareSize):
#         self.prompt = prompt
#         self.n = n
#         self.squareSize = squareSize

# model=Description("This is a test", 1, "512x512")

class ImageGenerator:
    def __init__(self):
        openai.api_key = os.getenv("API_KEY")
        self.APIKey=openai.api_key

    def generateImage(self,description:Description):
        openai.api_key = self.APIKey
        response=openai.Image.create(
        prompt = description.prompt,
        n = description.n,
        size = description.squareSize,
        )
        self.imageURL= response['data']
        # print(self.imageURL)
        self.imageURL=[image['url'] for image in self.imageURL]
        # return response
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


generate=ImageGenerator()
generate.generateImage()