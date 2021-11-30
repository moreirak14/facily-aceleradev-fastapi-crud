from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_api():
    return {"detail":"Hello World!"}


@app.get('/soma/{a}/{b}')
def soma(a: int, b: int):
    return {'resultado': a+b}


@app.post("/{message}")
def send_message(message: str):
    return message
