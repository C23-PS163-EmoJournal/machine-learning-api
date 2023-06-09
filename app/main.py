# import FastAPI
from fastapi import FastAPI, UploadFile
from app.module import *

app = FastAPI()

@app.get("/files/{file_path:path}")
def predict(file_path: str):
    emotion, confidence = prediction(file_path)
    
    return {
        "message": "200, Predict success",
        "Emotion": emotion,
        "Confidence": str(confidence)
    }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.get("/")
def main():
    return {"message": "Hello World"}