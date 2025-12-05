from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from litestar.dto import DTOConfig
from app.models import Book

class BookReadDTO(SQLAlchemyDTO[Book]):
    config = DTOConfig(exclude={"loans"})

class BookCreateDTO(SQLAlchemyDTO[Book]):
    config = DTOConfig(exclude={"id", "categories", "reviews", "loans"})

class BookUpdateDTO(SQLAlchemyDTO[Book]):
    config = DTOConfig(exclude={"id", "categories", "reviews", "loans"}, partial=True)