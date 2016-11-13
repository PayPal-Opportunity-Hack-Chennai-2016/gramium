from django.contrib import admin

# Register your models here.
from core.models import Account, Identity, Group, Member, Loan, Repayment


class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'get_group', 'bank', 'ifsc']

    search_fields = ('account_number',)

    def get_group(self, obj):
        return obj.group.name

    get_group.admin_order_field = 'name'  # Allows column order sorting
    get_group.short_description = 'Group Name'  # Renames column head

class AccountInline(admin.StackedInline):
    model = Account

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name','group_purpose',)
    inlines = [AccountInline, ]

class IdentityInline(admin.StackedInline):
    model = Identity
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'street_name', 'village', 'phone')
    inlines = [IdentityInline, ]

class LoanAdmin(admin.ModelAdmin):
    list_display = ('get_group', 'principal','remaining_installments')

    def get_group(self, obj):
        return obj.group.name

    get_group.admin_order_field = 'name'  # Allows column order sorting
    get_group.short_description = 'Group Name'  # Renames column head

class RepaymentAdmin(admin.ModelAdmin):
    list_display = ('get_group', 'get_principal','amount_paid','installment_number')

    def get_group(self, obj):
        return obj.loan.group.name

    get_group.admin_order_field = 'name'  # Allows column order sorting
    get_group.short_description = 'Group Name'  # Renames column head


    def get_principal(self, obj):
        return obj.loan.principal

    get_principal.admin_order_field = 'principal'  # Allows column order sorting
    get_principal.short_description = 'Loan Principal'  # Renames column head

# admin.site.register(Account, AccountAdmin)
admin.site.register(Group, GroupAdmin)
# admin.site.register(Identity)
admin.site.register(Member, MemberAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Repayment, RepaymentAdmin)

admin.site.site_header = "Gramium"
admin.site.site_title = "Admin | Gramium"
