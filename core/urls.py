from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'account',AccountViewSet)
router.register(r'group',GroupViewSet)
router.register(r'identity',IdentityViewSet)
router.register(r'loan',LoanViewSet)
router.register(r'repayment',RepaymentViewSet)
router.register(r'member',MemberViewSet)

