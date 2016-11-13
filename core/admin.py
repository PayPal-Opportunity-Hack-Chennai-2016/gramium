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
    list_display = ('name', 'village','phone')
    inlines = [IdentityInline, ]

class LoanInline(admin.ModelAdmin):
    list_display = ('get_group', 'village','phone')

    def get_group(self, obj):
        return obj.group.name

    get_group.admin_order_field = 'name'  # Allows column order sorting
    get_group.short_description = 'Group Name'  # Renames column head
    inlines = [IdentityInline, ]

admin.site.register(Account, AccountAdmin)
admin.site.register(Group, GroupAdmin)
# admin.site.register(Identity)
admin.site.register(Member, MemberAdmin)
admin.site.register(Loan)
admin.site.register(Repayment)

admin.site.site_header = "Gramium"
admin.site.site_title = "Admin | Gramium"
