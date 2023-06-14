# Speech Emotion Recognition API

## About
This is the API for Speech Emotion Recognition. It is an indepedent service that deployed only for machine learning hotel recommendation model.

| Information  | Value                                  |
|--------------|----------------------------------------|
| Docker Image | C23-PS163-EmoJournal/machine-learning-api |
|   Port Open  |                  80                  |

| Endpoint | Method |           Body Sent (JSON)          |                 Return                |
|:--------:|:------:|:-----------------------------------:|:------------------------------------------:|
|     /    |   GET  |                 None                |            "message": "Hello World"            |
|     /predict/{file_path:path}    |  GET  | file_path: str | return Emotion and Confidence in JSON |
|     /list_files/    |  GET  | None | {"files": files} |
|     /uploadfile/    |  POST  | file: UploadFile - FormData | "filename": file.filename, "filepath": dest |

## Build with
- Python 3.8.10
- FastAPI

## How to run
### First Option - local
make docker images with `docker build -t emojournal-ml-api:v1 .`
And then, 
run with `docker run --name container1 -p 80:80 emojournal-ml-api:v1`

### Second Option - Cloud Run
1. Go to dashboard Cloud Run, and then click `Create Service`
2. Select `Continuously deploy new revisions from a source repository` and then click `Set up with CLoud Build`.
3. Select `GitHub (Cloud Build GitHub App)`, this repository, and then click `Next`. 
4. Select branch `main` and bulid configuration `Dockerfile`, and then click `Save`.
5. In the `Container, Networking, and Security` section, see the `Container port` and set `80`.
6. Click `Create` and wait for the build process to complete.