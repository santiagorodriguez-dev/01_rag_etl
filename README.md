---
title: Chatbot RAG'S
description: Chatbot con información de RAGs sobre la Historia, Presente y Futuro de la IA (gpt-4o-mini de OpenAI)
---
# Chatbot RAG'S

## Características

- FastAPI
- [Hypercorn](https://hypercorn.readthedocs.io/)
- Python 3
- langChain, langSmith, langGraph
- SupaBase (PGVector con PostgreSQL)

## Base de Datos

- Esquema de Base de datos
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/BD_1.PNG)

- datos descargados
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/BD_2.PNG)

- Coleccion de vectores
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/BD_3.PNG)

- Fuentes urls
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/BD_4.PNG)

- Nombre coleccion
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/BD_5.PNG)

## ETL

- Diagrama ETL
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/etl.png)

## langSmith

- Template promt
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/template_prompt.PNG)

- Trazas ejecuciones del modelo
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/trazas_01.PNG)
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/trazas_02.PNG)

## Test Apis

- EndPoint load_data
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/api_01.PNG)

- EndPoint call_modelo
     
![imagen](https://github.com/santiagorodriguez-dev/rag_01_apis/blob/main/imagen/api_02.PNG)

## Cómo usar

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

