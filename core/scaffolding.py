from generic_scaffold import CrudManager
from core.models import Group, Member, Account, Identity, Loan, Repayment

class BookCrudManager(CrudManager):
    model = Group
    prefix = 'group/'