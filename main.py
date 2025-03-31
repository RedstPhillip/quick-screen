from fastapi import FastAPI

import data

app = FastAPI()


@app.get("/")
async def root():
    cpu_count = data.cpu_count()
    return {"cpu_count": cpu_count}


