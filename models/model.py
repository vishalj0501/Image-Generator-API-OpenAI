# from pydantic import BaseModel
from dataclasses import dataclass
from fastapi import Form

@dataclass
class Description():
    prompt:str=Form
    n: int = Form
    squareSize: str = Form