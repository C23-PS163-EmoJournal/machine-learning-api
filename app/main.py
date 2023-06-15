# import FastAPI
from fastapi import FastAPI, UploadFile, File
from app.module import *
import os
import shutil

from pathlib import Path
from google.cloud import storage
from google.cloud.exceptions import NotFound

app = FastAPI()

@app.get("/predict/{file_path:path}")
def predict(file_path: str):
    file_path = "/"+file_path
    emotion, confidence = prediction(file_path)
    
    return {
        "message": "200, Predict success",
        "Emotion": emotion,
        "Confidence": str(confidence)
    }

@app.get("/predict_from_bucket/{name}")
def download_predict(name: str):
    try:
        # set path to private key and make client
        path_to_private_key = '../code/assets/google-cloud-key.json'
        client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)
        bucket = storage.Bucket(client, 'file-suara')
        
        # make folder path
        path_folder = f'../code/downloads/{bucket.name}'
        Path(path_folder).mkdir(parents=True, exist_ok=True)

        # download file
        blob = bucket.blob(name)     
        blob.download_to_filename(f'{path_folder}/{blob.name}')
        # return f'{path_folder}/{blob.name}'

        # prediction
        emotion, confidence = prediction(f'{path_folder}/{blob.name}')
    
        return {
            "path_file": "{path_folder}/{blob.name}",
            "message": "200, Predict success",
            "Emotion": emotion,
            "Confidence": str(confidence)
        }
    
    except:
        return { f'{blob.name} does not exist - do something' }
        

# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     upload_dir = os.path.join(os.getcwd(), "../code/downloads/")
#     # Create the upload directory if it doesn't exist
#     if not os.path.exists(upload_dir):
#         os.makedirs(upload_dir)

#     # get the destination path
#     dest = os.path.join(upload_dir, file.filename)
#     print(dest)

#     # copy the file contents
#     with open(dest, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # return filename and file path
#     return {"filename": file.filename, "filepath": dest}

# # dapatkan list file dari folder uploads
# @app.get("/list_files/")
# async def get_list_files():
#     upload_dir = os.path.join(os.getcwd(), "../code/downloads/")
#     files = os.listdir(upload_dir)

#     files = [str(i+1)+". "+files[i] for i in range(len(files))]
#     return {"files": files}

@app.get("/")
def main():
    return {"message": "Hello World"}
