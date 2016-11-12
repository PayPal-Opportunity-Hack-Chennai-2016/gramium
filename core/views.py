from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from core.models import Member, Group
from core.serializers import GroupSerializer, MemberSerializer


class DisableCSRFOnDebug(object):
    pass

class GroupViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class MemberViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()