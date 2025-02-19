from fastapi import FastAPI

app = FastAPI()

@app.get("/load_data")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}