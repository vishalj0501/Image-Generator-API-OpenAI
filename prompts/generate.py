import os
import sys
import openai
import json
from dotenv import load_dotenv
from models.model import Description

load_dotenv()



sys.path.append(sys.path.append(sys.path[0] + "/.."))
class ImageGenerator:
    def __init__(self):
        openai.api_key = os.getenv("API_KEY")
        self.APIKey=openai.api_key
        self.imageURL=str

    def generateImage(self,description:Description):
        self.APIKey
        response=openai.Image.create(
        prompt = description.prompt,
        n = description.n,
        size = description.squareSize,
        )
        self.imageURL= response['data']
        self.imageURL=[image['url'] for image in self.imageURL]


generate=ImageGenerator()
generate.generateImage()