from loguru import logger
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import os
import face_recognition
import cv2
from loguru import logger
import pathlib as Path
import math
import cv2
import numpy as np
from PIL import Image
import io
import base64
import asyncio
import face_recognition
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import cv2
import face_recognition
import numpy as np
import os
import math
import asyncio
import aiohttp
import logging
import pathlib

from database.sqlalchemy import engine, session, base
from database.models import *
from inputs.yamnetrec import process_audio

base.metadata.create_all(engine)
current_session = session()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/yamnet")
# async def get_yamnet_result():
#     result = process_audio()
#     return {"result": result}

logger = logging.getLogger(__name__)


@app.get("/ws")
async def websocket_endpoint():
    async with WebSocket() as websocket:
        await websocket.accept()
