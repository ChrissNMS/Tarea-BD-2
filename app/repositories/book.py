from typing import Sequence
from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy import select, func
from app.models import Book, Category, Review

class BookRepository(SQLAlchemySyncRepository[Book]):
    model_type = Book

    def get_available_books(self) -> Sequence[Book]:
        return self.list(Book.stock > 0)

    def find_by_category(self, category_id: int) -> Sequence[Book]:
        statement = select(Book).join(Book.categories).where(Category.id == category_id)
        return self.list(statement)

    def get_most_reviewed_books(self, limit: int = 10) -> Sequence[Book]:
        statement = (
            select(Book)
            .join(Book.reviews)
            .group_by(Book.id)
            .order_by(func.count(Review.id).desc())
            .limit(limit)
        )
        return self.list(statement)

    def search_by_author(self, author_name: str) -> Sequence[Book]:
        return self.list(Book.title.ilike(f"%{author_name}%"))

    def update_stock(self, book_id: int, quantity: int) -> Book:
        book = self.get(book_id)
        if book.stock + quantity < 0:
            raise ValueError("Stock cannot be negative")
        book.stock += quantity
        return self.update(book)