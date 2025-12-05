from typing import Sequence
from litestar import Controller, get, post, put, delete, patch
from litestar.exceptions import HTTPException

from app.models import Book
from app.repositories.book import BookRepository
from app.dtos.book import BookReadDTO, BookCreateDTO, BookUpdateDTO

class BookController(Controller):
    path = "/books"
    tags = ["Books"]
    return_dto = BookReadDTO

    @get()
    async def list_books(self, book_repo: BookRepository) -> Sequence[Book]:
        return book_repo.list()

    @get("/available")
    async def get_available(self, book_repo: BookRepository) -> Sequence[Book]:
        """Libros con stock > 0"""
        return book_repo.get_available_books()

    @get("/search/{author_name:str}")
    async def search_by_author(self, author_name: str, book_repo: BookRepository) -> Sequence[Book]:
        return book_repo.search_by_author(author_name)

    @get("/category/{category_id:int}")
    async def find_by_category(self, category_id: int, book_repo: BookRepository) -> Sequence[Book]:
        return book_repo.find_by_category(category_id)
    
    @get("/most-reviewed")
    async def get_most_reviewed(self, book_repo: BookRepository) -> Sequence[Book]:
        return book_repo.get_most_reviewed_books()

    @post(dto=BookCreateDTO)
    async def create_book(self, data: Book, book_repo: BookRepository) -> Book:
        if data.stock < 1:
            raise HTTPException(status_code=400, detail="El stock inicial debe ser mayor a 0")
        return book_repo.add(data)

    @patch("/{book_id:int}", dto=BookUpdateDTO)
    async def update_book(self, book_id: int, data: Book, book_repo: BookRepository) -> Book:
        if data.stock is not None and data.stock < 0:
             raise HTTPException(status_code=400, detail="El stock no puede ser negativo")
        
        data.id = book_id
        return book_repo.update(data)