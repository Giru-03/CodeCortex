from django.db import models
from django.contrib.auth.models import User
import datetime


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title
    

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    zip_code = models.IntegerField()
    category = models.CharField(max_length=100, default="uncategorized")
    cc_num = models.CharField(max_length=16, default="0000000000000000")
    trans_day = models.IntegerField(default=datetime.datetime.now().day)
    trans_month = models.IntegerField(default=datetime.datetime.now().month)
    trans_year = models.IntegerField(default=datetime.datetime.now().year)
    trans_hour = models.IntegerField(default=datetime.datetime.now().hour)
    trans_minute = models.IntegerField(default=datetime.datetime.now().minute)
    blockchain_hash = models.CharField(max_length=256, null=True, blank=True)


    def __str__(self):
        return f"Transaction by {self.user} on {self.trans_day}/{self.trans_month}/{self.trans_year}"



# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils.translation import gettext_lazy as _
# from .managers import CustomUserManager

# class CustomUserModel(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('Email Address'), unique=True)
#     first_name = models.CharField(_('First Name'), max_length=100)
#     last_name = models.CharField(_('Last Name'), max_length=100, null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name','last_name','gender']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
