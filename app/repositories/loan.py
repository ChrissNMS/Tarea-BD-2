from datetime import date
from decimal import Decimal
from typing import Sequence
from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy import select
from app.models import Loan, LoanStatus, Book

class LoanRepository(SQLAlchemySyncRepository[Loan]):
    model_type = Loan

    def get_active_loans(self) -> Sequence[Loan]:
        """Req 51: préstamos activos"""
        return self.list(Loan.status == LoanStatus.ACTIVE)

    def get_overdue_loans(self) -> Sequence[Loan]:
        """Req 52: préstamos vencidos"""
        today = date.today()
        loans = self.list((Loan.status == LoanStatus.ACTIVE) & (Loan.due_date < today))
        for loan in loans:
            loan.status = LoanStatus.OVERDUE
            self.update(loan)
        return loans

    def calculate_fine(self, loan_id: int) -> Decimal:
        """Req 53: calcular multa ($500 por día)"""
        loan = self.get(loan_id)
        if not loan or not loan.due_date:
            return Decimal(0)
        today = date.today()
        if today > loan.due_date:
            days = (today - loan.due_date).days
            return Decimal(days * 500)
        return Decimal(0)

    def return_book(self, loan_id: int) -> Loan:
        """Req 54: procesar devolución"""
        loan = self.get(loan_id)
        fine = self.calculate_fine(loan_id)

        loan.status = LoanStatus.RETURNED
        loan.return_date = date.today()
        loan.fine_amount = fine
        self.update(loan)
        
        session = self.session
        book = session.get(Book, loan.book_id)
        if book:
            book.stock += 1
            session.add(book)
            
        return loan

    def get_user_loan_history(self, user_id: int) -> Sequence[Loan]:
        """Req 55: historial de usuario"""
        return self.list(Loan.user_id == user_id)