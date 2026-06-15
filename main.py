from fastapi import FastAPI

app = FastAPI()

def root():
    return "Up and running!"