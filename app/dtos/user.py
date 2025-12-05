from dataclasses import dataclass
from litestar.dto import DataclassDTO, DTOConfig
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from app.models import User

# --- 1. MODELO DE DATOS PARA LOGIN (Payload) ---
@dataclass
class LoginPayload:
    email: str
    password: str

# --- 2. DTO DE LOGIN (Configuración para Litestar) ---
# Esto arregla el error "AttributeError: ... create_for_field_definition"
class UserLoginDTO(DataclassDTO[LoginPayload]):
    config = DTOConfig()

# --- 3. DTOs DE LA TAREA (Tus requerimientos) ---

class UserReadDTO(SQLAlchemyDTO[User]):
    config = DTOConfig(exclude={"password", "loans", "reviews"})

class UserCreateDTO(SQLAlchemyDTO[User]):
    config = DTOConfig(exclude={"id", "is_active", "loans", "reviews"})

class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = DTOConfig(exclude={"id", "is_active", "loans", "reviews"}, partial=True)