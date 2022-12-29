from fastapi import FastAPI, UploadFile, File
import pandas as pd
import numpy as np
from model import *
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "this is SOM app ! "}
# method to import data set csv file
# la fonction prend les données avec les dimentions de la SOM
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

