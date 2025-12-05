from litestar import Controller, post
from litestar.exceptions import HTTPException
from litestar.security.jwt import OAuth2Login

from app.models import User
from app.repositories.user import UserRepository, password_hasher
from app.dtos.user import UserLoginDTO, LoginPayload 

class AuthController(Controller):
    path = "/login"
    tags = ["Auth"]

    @post(dto=UserLoginDTO)
    async def login(self, data: LoginPayload, user_repo: UserRepository) -> OAuth2Login:
        user = user_repo.get_one_or_none(email=data.email)
        
        if not user or not password_hasher.verify(data.password, user.password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        
        return OAuth2Login(user=user)