from typing import Sequence
from litestar import Controller, get, post, put, delete
from app.models import Category
from app.repositories.category import CategoryRepository
from app.dtos.category import CategoryReadDTO, CategoryCreateDTO, CategoryUpdateDTO

class CategoryController(Controller):
    path = "/categories"
    tags = ["Categories"]
    return_dto = CategoryReadDTO

    @get()
    async def list_categories(self, category_repo: CategoryRepository) -> Sequence[Category]:
        return category_repo.list()

    @get("/{category_id:int}")
    async def get_category(self, category_id: int, category_repo: CategoryRepository) -> Category:
        return category_repo.get(category_id)

    @post(dto=CategoryCreateDTO)
    async def create_category(self, data: Category, category_repo: CategoryRepository) -> Category:
        return category_repo.add(data)

    @put("/{category_id:int}", dto=CategoryUpdateDTO)
    async def update_category(self, category_id: int, data: Category, category_repo: CategoryRepository) -> Category:
        data.id = category_id
        return category_repo.update(data)

    @delete("/{category_id:int}")
    async def delete_category(self, category_id: int, category_repo: CategoryRepository) -> None:
        category_repo.delete(category_id)