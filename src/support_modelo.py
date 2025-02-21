import sys
sys.path.append("../")
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_core.tools import tool
from langchain_postgres import PGVector
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain import hub

from src import support_bd as bd

def load_data_rag_bd(collection_name):
    
    try:
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_NAME = os.getenv("DB_NAME")
        HOST = os.getenv("HOST")

        conn_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{HOST}:5432/{DB_NAME}"

        return PGVector(
            embeddings=embeddings,
            collection_name=collection_name,
            connection=conn_string,
        )

    except Exception as e:
        print(e)
    

@tool(response_format="content_and_artifact")
def retrieve(query: str):
    """Retrieve information related to a query."""
    supabase_client = bd.init_conection_bd()
    coleccion = bd.select_datos("coleccion", supabase_client)
    collection_name = coleccion.data[0].get("name_coleccion")
    vector_store_load = load_data_rag_bd(collection_name)
    retrieved_docs = vector_store_load.similarity_search(query, k=4)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


def create_react_agent_func():
    
    system_prompt = (hub.pull("danteboxs/ai_assistant_rag").template)

    memory = MemorySaver()

    llm = init_chat_model("gpt-4o-mini", model_provider="openai")

    return create_react_agent(llm, tools=[retrieve], checkpointer=memory, prompt=system_prompt)

def call_modelo_func(input_message: str, thread_id: str, user_id: str, agent_executor):

    config = {"configurable": {"thread_id": thread_id, "user_id": user_id}}

    for event in agent_executor.stream(
        {"messages": [{"role": "user", "content": input_message}]},
        stream_mode="values",
        config=config,
    ):pass

    mesajes_trazas = ""
    for e in event["messages"]:
        mesajes_trazas = mesajes_trazas + e.pretty_repr() + '\n\n'

    return event["messages"][-1].content,  mesajes_trazas

