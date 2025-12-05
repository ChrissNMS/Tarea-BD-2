import re
from typing import Sequence
from litestar import Controller, get, post, put, delete, patch
from litestar.exceptions import HTTPException

from app.models import User
from app.repositories.user import UserRepository
from app.dtos.user import UserReadDTO, UserCreateDTO, UserUpdateDTO

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

class UserController(Controller):
    path = "/users"
    tags = ["Users"]
    return_dto = UserReadDTO

    @get()
    async def list_users(self, user_repo: UserRepository) -> Sequence[User]:
        return user_repo.list()

    @get("/{user_id:int}")
    async def get_user(self, user_id: int, user_repo: UserRepository) -> User:
        return user_repo.get(user_id)

    @post(dto=UserCreateDTO)
    async def create_user(self, data: User, user_repo: UserRepository) -> User:
        if not re.match(EMAIL_REGEX, data.email):
            raise HTTPException(status_code=400, detail="Formato de email inválido")
        return user_repo.add(data)

    @patch("/{user_id:int}", dto=UserUpdateDTO)
    async def update_user(self, user_id: int, data: User, user_repo: UserRepository) -> User:
        if data.email and not re.match(EMAIL_REGEX, data.email):
             raise HTTPException(status_code=400, detail="Formato de email inválido")
        
        data.id = user_id
        return user_repo.update(data)