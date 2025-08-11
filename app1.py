from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "app1"}


@app.get("/health")
async def health():
    return {"status": "OK"}