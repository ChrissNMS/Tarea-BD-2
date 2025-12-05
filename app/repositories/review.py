from advanced_alchemy.repository import SQLAlchemySyncRepository
from app.models import Review

class ReviewRepository(SQLAlchemySyncRepository[Review]):
    model_type = Review