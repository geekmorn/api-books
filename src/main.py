from fastapi import FastAPI

app = FastAPI(docs_url='/')


@app.get('/')
def hi_world():
    return 'Hi world!'
