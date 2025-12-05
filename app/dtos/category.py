from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from litestar.dto import DTOConfig
from app.models import Category

class CategoryReadDTO(SQLAlchemyDTO[Category]):
    config = DTOConfig(exclude={"books"})

class CategoryCreateDTO(SQLAlchemyDTO[Category]):
    config = DTOConfig(exclude={"id", "books"})

class CategoryUpdateDTO(SQLAlchemyDTO[Category]):
    config = DTOConfig(exclude={"id", "books"}, partial=True)