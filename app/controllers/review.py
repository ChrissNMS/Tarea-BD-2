from typing import Sequence
from litestar import Controller, get, post, delete
from litestar.exceptions import HTTPException

from app.models import Review
from app.repositories.review import ReviewRepository
from app.dtos.review import ReviewReadDTO, ReviewCreateDTO

class ReviewController(Controller):
    path = "/reviews"
    tags = ["Reviews"]
    return_dto = ReviewReadDTO

    @get()
    async def list_reviews(self, review_repo: ReviewRepository) -> Sequence[Review]:
        return review_repo.list()

    @post(dto=ReviewCreateDTO)
    async def create_review(self, data: Review, review_repo: ReviewRepository) -> Review:
        if data.rating < 1 or data.rating > 5:
            raise HTTPException(status_code=400, detail="El rating debe ser entre 1 y 5")
        
        return review_repo.add(data)

    @delete("/{review_id:int}")
    async def delete_review(self, review_id: int, review_repo: ReviewRepository) -> None:
        review_repo.delete(review_id)