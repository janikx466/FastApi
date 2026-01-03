from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"hello": "this is home page"}

@app.get("/health")
def health():
    return {"status": "ok"}
