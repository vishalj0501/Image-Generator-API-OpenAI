from prompts.generate import ImageGenerator
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
import sys
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.append(sys.path[0] + "/..")

app = FastAPI()
router = APIRouter()

imageGen=ImageGenerator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router.add_api_route(
    "api/generate",
    endpoint=imageGen.generateImage,
    methods=["POST"]
)
app.include_router(router)

if __name__ == "__main__":
    