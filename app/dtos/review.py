from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from litestar.dto import DTOConfig
from app.models import Review

class ReviewReadDTO(SQLAlchemyDTO[Review]):
    config = DTOConfig(max_nested_depth=1)

class ReviewCreateDTO(SQLAlchemyDTO[Review]):
    config = DTOConfig(exclude={"id", "review_date", "user", "book"})