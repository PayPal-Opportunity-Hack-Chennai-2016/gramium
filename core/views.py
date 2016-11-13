from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from core.models import Member, Group, Account, Identity, Loan, Repayment
from core.serializers import GroupSerializer, MemberSerializer, AccountSerializer, IdentitySerializer, LoanSerializer, \
    RepaymentSerializer


class DisableCSRFOnDebug(object):
    pass

class AccountViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class GroupViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class IdentityViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = IdentitySerializer
    queryset = Identity.objects.all()

class LoanViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

class MemberViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class RepaymentViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = RepaymentSerializer
    queryset = Repayment.objects.all()