from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Up and running!"