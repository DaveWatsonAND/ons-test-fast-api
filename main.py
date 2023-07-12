# main.py
from fastapi import FastAPI
from api import survey
from api import template

app = FastAPI()
app.include_router(survey.router)
app.include_router(template.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
