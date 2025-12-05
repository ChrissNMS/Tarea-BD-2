from datetime import date, timedelta
from typing import Sequence
from litestar import Controller, get, post, patch
from litestar.exceptions import HTTPException

from app.models import Loan, LoanStatus
from app.repositories.loan import LoanRepository
from app.dtos.loan import LoanReadDTO, LoanCreateDTO, LoanUpdateDTO

class LoanController(Controller):
    path = "/loans"
    tags = ["Loans"]
    return_dto = LoanReadDTO

    @get()
    async def list_loans(self, loan_repo: LoanRepository) -> Sequence[Loan]:
        return loan_repo.list()
    
    @get("/overdue")
    async def get_overdue(self, loan_repo: LoanRepository) -> Sequence[Loan]:
        return loan_repo.get_overdue_loans()

    @get("/user/{user_id:int}")
    async def get_user_history(self, user_id: int, loan_repo: LoanRepository) -> Sequence[Loan]:
        return loan_repo.get_user_loan_history(user_id)

    @post(dto=LoanCreateDTO)
    async def create_loan(self, data: Loan, loan_repo: LoanRepository) -> Loan:
        data.loan_date = date.today()
        data.due_date = date.today() + timedelta(days=14)
        data.status = LoanStatus.ACTIVE
        
        return loan_repo.add(data)

    @post("/{loan_id:int}/return")
    async def return_book(self, loan_id: int, loan_repo: LoanRepository) -> Loan:
        return loan_repo.return_book(loan_id)