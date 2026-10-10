from fastapi import APIRouter, Path, HTTPException, status
from model import Book, BookItem, BookItems

todo_router = APIRouter()
book_list = []

@todo_router.post("/book", status_code=201)
async def add_book(book: Book) -> dict:
    book_list.append(book)
    return {"message": "Book added successfully by Vorontsov Nikita"}

@todo_router.get("/book", response_model=BookItems)
async def retrieve_books() -> dict:
    return {"books": book_list}

@todo_router.get("/book/{book_id}")
async def get_single_book(book_id: int = Path(..., title="The ID of the book to retrieve")) -> dict:
    for book in book_list:
        if book.id == book_id:
            return {"book": book}
   
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book with supplied ID doesn't exist."
    )


@todo_router.put("/book/{book_id}")
async def update_book(book_data: BookItem, book_id: int = Path(..., title="The ID of the book to be updated")) -> dict:
    for book in book_list:
        if book.id == book_id:
            book.title = book_data.title
            book.author = book_data.author
            return {"message": "Book updated successfully by Vorontsov Nikita"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book with supplied ID doesn't exist."
    )

@todo_router.delete("/book/{book_id}")
async def delete_single_book(book_id: int) -> dict:
    for index in range(len(book_list)):
        book = book_list[index]
        if book.id == book_id:
            book_list.pop(index)
            return {"message": "Book deleted successfully by Vorontsov Nikita"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book with supplied ID doesn't exist."
    )

@todo_router.delete("/book")
async def delete_all_books() -> dict:
    book_list.clear()
    return {"message": "All books deleted successfully by Vorontsov Nikita"}