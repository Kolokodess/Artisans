from django.db import models
from .choices import SKILL_SET, ACC_SET, GENDER
from django.contrib.auth.models import User

# models
class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True )
    address = models.CharField(max_length = 100, blank = True)
    lga = models.CharField(max_length = 40, blank = True)
    state = models.CharField(max_length = 40, blank = True)
    country = models.CharField(max_length = 40,  blank = True)

    def __str__(self):
        return self.address

class BankDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length = 50)
    acc_name = models.CharField(max_length = 50)
    acc_num = models.IntegerField()

    def __str__(self):
        return self.bank_name

class Occcupation(models.Model):
    user = models.ManyToManyField(User)
    occcupation = models.CharField(max_length = 40, choices = SKILL_SET)
    skill = models.CharField(max_length = 120)

    def __str__(self):
        return self.skill

class Company(models.Model):
    name = models.CharField(max_length = 120)
    tel = models.CharField(max_length = 120)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

class Affiliate(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.IntegerField(null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    acc_type = models.CharField(max_length = 15, choices  = ACC_SET)
    gender = models.CharField(max_length = 10, choices = GENDER, null = True, blank =True)
    date_of_birth = models.DateField(null = True, blank =True)
    organisation = models.ForeignKey(Company, null = True, blank =True)
    affiliate = models.ManyToManyField(Affiliate, null = True, blank = True )

    def __str__(self):
        return self.user.__str__()

#
# class CompanyAddress(models.Model):
#     company = models.ForeignKey(Company)
#     address = models.CharField(max_length = 100, blank = True)
#     lga = models.CharField(max_length = 40, blank = True)
#     state = models.CharField(max_length = 40, blank = True)
#     country = models.CharField(max_length = 40,  blank = True)
#
#     def __str__(self):
#         return self.address
