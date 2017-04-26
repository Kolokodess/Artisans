from django.contrib import admin
from .models import UserAccount, Address
from django.contrib.auth.models import User

#admin.site.register(User)
admin.site.register(UserAccount)
admin.site.register(Address)

# Register your models here.
