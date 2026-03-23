from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/hello")
def hello(name = "Yashwanth"):
    return {"message": f"Hello, {name}"}
