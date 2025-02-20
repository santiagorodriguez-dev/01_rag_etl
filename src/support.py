import sys
sys.path.append("../")
import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from fake_useragent import UserAgent

from langchain_postgres import PGVector
import re

from src import support_bd as bd

def limpiar_string(texto):
    # 1. Mantener solo letras, números, acentos, ñ, puntos y espacios
    try:
        texto_limpio = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ. ]', ' ', texto)
        # 2. Reemplazar múltiples espacios por uno solo
        texto_limpio = re.sub(' +', ' ', texto_limpio)
        return texto_limpio
    except Exception as e:
        print(e)
        return ""

def download_insert_data_bd():
    
    try:
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_NAME = os.getenv("DB_NAME")
        HOST = os.getenv("HOST")

        conn_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{HOST}:5432/{DB_NAME}"

        supabase_client = bd.init_conection_bd()
        urls = bd.select_datos("fuentes_urls", supabase_client)
        coleccion = bd.select_datos("coleccion", supabase_client)

        collection_name = coleccion.data[0].get("name_coleccion")

        url_list = []
        for u in urls.data:
            url_list.append(u.get("url"))

        vector_store_input = PGVector(
            embeddings=embeddings,
            collection_name=collection_name,
            connection=conn_string,
        )

        ua = UserAgent()
        os.environ["USER_AGENT"] = ua.random

        loader = WebBaseLoader(url_list)
        
        docs = loader.load()

        for d in docs:
            d.page_content = limpiar_string(d.page_content)

        print(f"Total docs: {len(docs)}")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
        all_splits = text_splitter.split_documents(docs)

        # Index chunks
        indices_documentos = vector_store_input.add_documents(documents=all_splits)
        print(f"Total docs spliteados: {len(indices_documentos)}")

        return docs, len(indices_documentos), collection_name
    
    except Exception as e:
        print(e)
    