from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=30)
    account_number = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    account_type = models.CharField(max_length=30)

class Group(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    account = models.ForeignKey(to="Account")

class Identity(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)

class Member(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    phone = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    is_incharge = models.BooleanField(default=False)
    id_proof = models.ForeignKey(to="Identity")
    group  = models.ForeignKey(to="Group")
    is_active = models.BooleanField(default=True)

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

class RePayment(models.Model):
    monthly_amount = models.DecimalField(decimal_places=2, max_digits=8)
    installment_number = models.IntegerField()
    date_paid = models.DateField()