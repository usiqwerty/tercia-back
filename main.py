from fastapi import FastAPI

from dblevel import Database

app = FastAPI()
db = Database()
db.connect()


@app.get("/")
async def root():
    return list(db.get_courses())
