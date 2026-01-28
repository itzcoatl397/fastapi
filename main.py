from fastapi import FastAPI, HTTPException
from fastapi.params import Query, Body
from pydantic import BaseModel

from schemas.post_schema import PostBase, PostCreate, PostUpdate

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
def create_post(post: PostCreate):
    new_id = (POSTS[-1]["id"] + 1) if post else 1
    new_post = {
        "id": new_id,
        "title": post.title,
        "content":post.content,
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
        postJson:PostUpdate,
):
    for post in POSTS:
        if post["id"] == id:

            playload = postJson.model_dump(exclude_unset=True)

            if "title" in playload: post["title"] = postJson["title"]

            if "content" in playload: post["content"] = postJson["content"]
            return {
                "status_code": 200,
                "message": "Post updated successfully",
                "data": post
            }
    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{id}")

def delete_post(id: int,status_code = 204):
    for index,post in enumerate(POSTS):
        if post["id"] == id:
            POSTS.pop(index)
            return

    raise HTTPException(status_code=404, detail="Post not found")



