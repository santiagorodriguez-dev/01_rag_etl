from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
sys.path.append("../")
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

app = FastAPI()

class DataModel(BaseModel):
    code: str


@app.post("/load_data")
async def load_data(data: DataModel):
    try:
        if data.code == os.getenv("secret"):
            return {"message": "Data loaded successfully"}
        else:
            return HTTPException(status_code=401, detail="Unauthorized", headers={"Authenticate": "Key not valid"})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e), headers={"Error General": "Algo ha ido mal"})