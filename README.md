---
title: Chatbot RAG'S
description: Chatbot con información de RAGs sobre la Historia, Presente y Futuro de la IA (gpt-4o-mini de OpenAI)
---
# Chatbot RAG'S

## Características

- FastAPI
- Hypercorn
- Python 3
- langChain, langSmith, langGraph
- SupaBase (PGVector con PostgreSQL)

## Base de Datos

- Esquema de Base de datos
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/BD_1.PNG)

- datos descargados
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/BD_2.PNG)

- Coleccion de vectores
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/BD_3.PNG)

- Fuentes urls
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/BD_4.PNG)

- Nombre coleccion
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/BD_5.PNG)

## ETL

- Diagrama ETL
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/etl.png)

## langSmith

- Template promt
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/template_prompt.PNG)

- Trazas ejecuciones del modelo
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/trazas_01.PNG)
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/trazas_02.PNG)

## Test Apis

- EndPoint load_data
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/api_01.PNG)

- EndPoint call_modelo
     
![images](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/images/api_02.PNG)

## Cómo usar

- Hay un fichero .env.example en el raiz del proyecto, renombrar sin el .example y cambiar por los datos correctos.

- Crear un entorno virtual 
```bash
python -m venv venv
```
- Activar el entorno virtual en Windows
```bash
venv\Scripts\activate
```
- Activar el entorno virtual en macOS/Linux
```bash
source venv/bin/activate
```
- Clonar el repositorio localmente e instalar paquetes con pip 
```bash
pip install -r requirements.txt
```
- Ejecutar localmente usando 
```bash
hypercorn main:app --reload
```

## Autores ✒️

* **Santiago Rodriguez** - [santiagorodriguez-dev](https://github.com/santiagorodriguez-dev)

