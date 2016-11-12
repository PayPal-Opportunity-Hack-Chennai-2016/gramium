from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=35, db_index=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=30)
    account_number = models.CharField(max_length=30)
    bank = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    account_type = models.CharField(max_length=30)
    group = models.ForeignKey(to = "Group")

    def __str__(self):
        return self.name+self.bank

class Member(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    phone = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    is_incharge = models.BooleanField(default=False)
    group  = models.ForeignKey(to="Group")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Identity(models.Model):
    id_type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    member = models.ForeignKey(to="Member")

    def __str__(self):
        return self.member.name + self.id_type

class Loan(models.Model):
    date = models.DateField()
    account = models.ForeignKey(to="Account")
    group = models.ForeignKey(to="Group")
    principal = models.DecimalField(decimal_places=2, max_digits=8)
    rate_of_interest = models.DecimalField(decimal_places=2, max_digits=8)
    number_of_installments = models.DecimalField(decimal_places=2, max_digits=8)
    monthly_installment = models.DecimalField(decimal_places=2, max_digits=8)
    remaining_amount = models.DecimalField(decimal_places=2, max_digits=8)
    remaining_installments = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.group.name

class Repayment(models.Model):
    monthly_amount = models.DecimalField(decimal_places=2, max_digits=8)
    installment_number = models.IntegerField()
    date_paid = models.DateField()
    loan = models.ForeignKey(to= "Loan")

    def __str__(self):
        return