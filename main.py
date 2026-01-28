from fastapi import FastAPI
from fastapi.params import Query, Body

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
def get_post(
        id: int,
        include_content: bool = Query(default=False, description="Incluir contenido completo")
):
    for post in POSTS:
        if post["id"] == id:
            if not include_content:
                return {
                    "id": post["id"],
                    "title": post["title"],
                }
            return {
                "data": post
            }

    return {
        "error": "Post not found"
    }


@app.post("/posts")
def create_post(post: dict = Body(...)):
    if "title" not in post or "content" not in post:
        return {"error", "Title  y Content son requerido"}

    if not str(post["title"]).strip():
        return {"error", "Title no puede estar vacio"}


    new_id =(POSTS[-1]["id"] + 1) if post else 1
    new_post = {
        "id": new_id,
        "title": post["title"],
        "content": post["content"]
    }
    POSTS.append(new_post)

    return {

        "status_code": 201,
        "message": "Post created successfully",
        "data": new_post,
    }



@app.put("/posts/{id}")
def update_post(
        id: int,
        postJson: dict = Body(...),
):
    if "title" not in postJson or "content" not in postJson:
        return {"error", "Title  y Content son requerido"}

    if not str(postJson["title"]).strip():
        return {"error", "Title no puede estar vacio"}


    for post in POSTS:
        if post["id"] == id:

            post["title"] = postJson["title"]
            post["content"] = postJson["content"]





