from fastapi import FastAPI
from fastapi.params import Query

app = FastAPI()

POSTS = [
    {
        "id": 1,
        "title": "FastAPI básico",
        "content": "Aprendiendo FastAPI paso a paso"
    },
    {
        "id": 2,
        "title": "Qué es una API",
        "content": "Introducción a las APIs REST"
    },
    {
        "id": 3,
        "title": "HTTP methods",
        "content": "GET, POST, PUT y DELETE explicados"
    },
    {
        "id": 4,
        "title": "Pydantic models",
        "content": "Validación de datos en FastAPI"
    },
    {
        "id": 5,
        "title": "Swagger UI",
        "content": "Documentación automática con FastAPI"
    },
    {
        "id": 6,
        "title": "Path parameters",
        "content": "Cómo usar parámetros en la URL"
    },
    {
        "id": 7,
        "title": "Query parameters",
        "content": "Filtrar datos con queries"
    },
    {
        "id": 8,
        "title": "Status codes",
        "content": "Códigos de estado HTTP más usados"
    },
    {
        "id": 9,
        "title": "FastAPI vs Flask",
        "content": "Comparación entre frameworks Python"
    },
    {
        "id": 10,
        "title": "Proyecto final",
        "content": "Creando una API completa con FastAPI"
    }
]


@app.get("/")
def main():
    return {"message": "Bienvenidos a  mi blog"}


@app.get("/posts")
def posts(query: str | None = Query(default=None, description="Query para obtener datos")):
    if query:
        results = [post for post in POSTS if query.lower() in post["title"].lower()]
        return {
            "results": results,
            "query": query,
        }
    return {
        "data": POSTS,
    }


@app.get("/posts/{id}")
def get_post(id: int):
    data = {}
    for post in POSTS:
        if post["id"] == id:
           return  {
               "data": post,
           }
    return {
        "error":"Post not found",
    }
