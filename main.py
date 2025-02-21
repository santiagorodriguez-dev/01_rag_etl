from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
sys.path.append("../")
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

from src import support as sp
from src import support_modelo as spm

app = FastAPI()
agent_executor = spm.create_react_agent_func()

class DataModel(BaseModel):
    code: str

class DataModelPrompt(BaseModel):
    code: str
    input_message: str
    thread_id: str
    user_id: str


@app.post("/load_data")
async def load_data(data: DataModel):
    try:
        if data.code == os.getenv("secret"):
            docs, indices_documentos, collection_name = sp.download_insert_data_bd()
            return {"num_doc": len(docs), 
                    "total_split_docs": indices_documentos,
                    "collection_name": collection_name, 
                    "docs_loads": docs,
                    "message": "Data loaded successfully"}
        else:
            return HTTPException(status_code=401, detail="Unauthorized", headers={"Authenticate": "Key not valid"})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e), headers={"Error General": "Algo ha ido mal"})
    

@app.post("/call_modelo")
async def call_modelo(data: DataModelPrompt):
    try:
        if data.code == os.getenv("secret"):
            content, mesajes_trazas = spm.call_modelo_func(data.input_message, data.thread_id, data.user_id, agent_executor)
            return {
                "content": content,
                "mesajes_trazas": mesajes_trazas,
                "message": "Data loaded successfully"
                }
        else:
            return HTTPException(status_code=401, detail="Unauthorized", headers={"Authenticate": "Key not valid"})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e), headers={"Error General": "Algo ha ido mal"})


