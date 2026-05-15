from fastapi import FastAPI

app = FastAPI(title='dip code test')


@app.get("/")
async def root():
    return {"status": "ok"}
