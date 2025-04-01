from fastapi import FastAPI

import data

app = FastAPI()


@app.get("/")
async def root():
    cpu_count = data.cpu_count()
    return {"cpu_count": cpu_count}


@app.get("/cpu-stats")
async def cpu_stats():
    cpu_stats = data.cpu_stats()
    print(cpu_stats)
    return {"cpu_stats": cpu_stats}
