from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def wellcom():
    return {
        "messages": "hello world"
    }



