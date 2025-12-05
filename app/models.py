from datetime import date
from enum import Enum
from typing import Optional, List
from decimal import Decimal
from dataclasses import dataclass

from sqlalchemy import ForeignKey, String, Text, Integer, Table, Boolean, Numeric, Column, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

@dataclass
class BookStats:
    total_books: int = 0
    total_loans: int = 0

@dataclass
class PasswordUpdate:
    current_password: str
    new_password: str

book_categories = Table(
    "book_categories",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
)

class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    books: Mapped[List["Book"]] = relationship(
        secondary=book_categories, back_populates="categories"
    )

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255)) 
    email: Mapped[str] = mapped_column(String(255), unique=True)
    phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    reviews: Mapped[List["Review"]] = relationship(back_populates="user")
    loans: Mapped[List["Loan"]] = relationship(back_populates="user")

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    author_id: Mapped[int] = mapped_column(Integer) 

    stock: Mapped[int] = mapped_column(Integer, default=1)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    language: Mapped[str] = mapped_column(String(2)) 
    publisher: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    categories: Mapped[List["Category"]] = relationship(
        secondary=book_categories, back_populates="books"
    )
    reviews: Mapped[List["Review"]] = relationship(back_populates="book")
    loans: Mapped[List["Loan"]] = relationship(back_populates="book")

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(Text)
    review_date: Mapped[date] = mapped_column(default=date.today)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    user: Mapped["User"] = relationship(back_populates="reviews")
    book: Mapped["Book"] = relationship(back_populates="reviews")

# --- MODELO LOAN ---
class LoanStatus(str, Enum):
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"

class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    loan_date: Mapped[date] = mapped_column(default=date.today)
    return_date: Mapped[Optional[date]] = mapped_column(nullable=True)
    
    due_date: Mapped[date] = mapped_column(Date) 
    
    fine_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 2), nullable=True)
    status: Mapped[LoanStatus] = mapped_column(default=LoanStatus.ACTIVE)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    user: Mapped["User"] = relationship(back_populates="loans")
    book: Mapped["Book"] = relationship(back_populates="loans")