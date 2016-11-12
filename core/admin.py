from django.contrib import admin

# Register your models here.
from core.models import Account, Identity, Group, Member, Loan, Repayment



admin.site.register(Account)
admin.site.register(Group)
admin.site.register(Identity)
admin.site.register(Member)
admin.site.register(Loan)
admin.site.register(Repayment)

admin.site.site_header = "Gramium"
admin.site.site_title = "Admin | Gramium"