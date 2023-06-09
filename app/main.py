# import FastAPI
from fastapi import FastAPI, UploadFile, File
from app.module import *
import os
import shutil

app = FastAPI()

@app.get("/files/{file_path:path}")
def predict(file_path: str):
    file_path = "/"+file_path
    emotion, confidence = prediction(file_path)
    
    return {
        "message": "200, Predict success",
        "Emotion": emotion,
        "Confidence": str(confidence)
    }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    upload_dir = os.path.join(os.getcwd(), "uploads")
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    # copy the file contents
    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}

@app.get("/")
def main():
    return {"message": "Hello World"}
