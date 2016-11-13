from __future__ import unicode_literals

import calendar
from datetime import timedelta, datetime
from django.db import models
import datetime
import calendar
# Create your models here.
from django.db.models import Model


class Group(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    noc_bank_status_check  = models.CharField(default = "Not Verified", max_length=30)
    description = models.TextField(blank=True, null=True)
    group_purpose = models.CharField(max_length=300, blank=True, null=True)
    send_sms_to_all_in_group = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=30)
    account_number = models.CharField(max_length=30)
    bank = models.CharField(max_length=300)
    branch = models.CharField(max_length=300)
    ifsc = models.CharField(max_length=30)
    account_type = models.CharField(max_length=30)
    group = models.OneToOneField(to = "Group")

    def __str__(self):
        return self.name+self.bank

class Member(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    phone = models.CharField(max_length=20)
    door_no = models.CharField(max_length=10, blank=True, null=True)
    street_name = models.CharField(max_length=50, blank=True, null=True)
    village = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    is_incharge = models.BooleanField(default=False)
    group  = models.ForeignKey(to="Group")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Identity(models.Model):
    id_type = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    member = models.ForeignKey(to="Member")

    def __str__(self):
        return self.member.name + self.id_type

class Loan(models.Model):
    date = models.DateField()
    group = models.ForeignKey(to="Group")
    principal = models.DecimalField(decimal_places=2, max_digits=8)
    rate_of_interest = models.DecimalField(decimal_places=2, max_digits=8)
    number_of_installments = models.DecimalField(decimal_places=2, max_digits=8)
    monthly_installment = models.DecimalField(decimal_places=2, max_digits=8,)
    remaining_amount = models.DecimalField(decimal_places=2, max_digits=8, blank=True)
    remaining_installments = models.IntegerField(blank=True)
    due_date = models.DateField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.group.name


    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = int(sourcedate.year + month / 12)
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.remaining_amount = self.principal
            self.remaining_installments = self.number_of_installments
            # self.due_date = self.date + timedelta(days=30)
            self.due_date = self.add_months(self.date, 1)
        super(Loan, self).save(*args, **kwargs)

class Repayment(models.Model):
    amount_paid = models.DecimalField(decimal_places=2, max_digits=8)
    installment_number = models.IntegerField()
    number_of_installments_paid = models.IntegerField()
    date_paid = models.DateField()
    loan = models.ForeignKey(to= "Loan")

    def __str__(self):
        return  unicode(self.installment_number) +self.loan.group.name

    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = int(sourcedate.year + month / 12)
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)

    def save(self, *args, **kwargs):
        if not self.pk:
            print "Helo"
            self.loan.remaining_amount = self.loan.remaining_amount - self.amount_paid
            self.loan.remaining_installments = self.loan.remaining_installments - self.number_of_installments_paid
            self.loan.due_date = self.add_months(self.loan.due_date,self.number_of_installments_paid)
            if self.loan.remaining_installments <= 0 or self.loan.remaining_amount <= 0:
                self.loan.is_active  = False
            self.loan.save()
        super(Repayment, self).save(*args, **kwargs)