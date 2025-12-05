from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from litestar.dto import DTOConfig
from app.models import Loan

class LoanReadDTO(SQLAlchemyDTO[Loan]):
    config = DTOConfig(max_nested_depth=1)

class LoanCreateDTO(SQLAlchemyDTO[Loan]):
    config = DTOConfig(
        exclude={
            "id", 
            "loan_date", 
            "return_date", 
            "due_date", 
            "fine_amount", 
            "status", 
            "user", 
            "book"
        }
    )

class LoanUpdateDTO(SQLAlchemyDTO[Loan]):
    config = DTOConfig(include={"status"}, partial=True)