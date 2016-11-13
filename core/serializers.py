from rest_framework import serializers

from core.models import Group, Member, Account, Identity, Loan, Repayment


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('pk','name', 'bank','account_number','branch','ifsc','account_type', 'group_id')

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('pk','name')

class IdentitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Identity
        fields = ('pk','id_type','number')

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('pk','name','phone','address1','address2','is_incharge','group','is_active')

class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ('pk','date','account','group','principal','rate_of_interest','number_of_installments','monthly_installment','remaining_amount','remaining_installments','is_active')

class RepaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repayment
        fields = ('pk', 'amount_paid','installment_number','date_paid')

