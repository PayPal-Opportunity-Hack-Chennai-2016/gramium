from rest_framework import serializers

from core.models import Group, Member


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('pk','name','loan_eligibility','account_number','incharge','incharge2')

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('pk','name','age','phone','address1','address2')

