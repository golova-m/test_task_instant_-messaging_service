from fastapi import FastAPI


app = FastAPI()


@app.get('/start')
def get_start():
    return {'data': 'Hello, world!'}