from pydantic import BaseModel
from typing import List

# Создания книги
class Book(BaseModel):
    id: int
    title: str
    author: str

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "id": 1,
                "title": "Мастер и Маргарита",
                "author": "Миахаил Афанасьевич Булгаков"
            }]
        }
    }

# Обновления книги
class BookItem(BaseModel):
    title: str
    author: str

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "title": "Дело утоплениц",
                "author": "Софья Ведищева Эвербук"
            }]
        }
    }

# Ответа из списка книг (скрывает ID)
class BookItems(BaseModel):
    books: List[BookItem]

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "books": [
                    {"title": "Мастер и Маргарита", "author": "Миахаил Афанасьевич Булгаков"},
                    {"title": "Дело утоплениц", "author": "Софья Ведищева Эвербук"}
                ]
            }]
        }
    }