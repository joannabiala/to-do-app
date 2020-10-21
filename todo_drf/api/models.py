from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max)



















#-------------------------------------------------
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
# # Create your models here.
#
# class Task(models.Model):
#   title = models.CharField(max_length=200)
#   completed = models.BooleanField(default=False, blank=True, null=True)
#
#   def __str__(self):
#     return self.title
#
# class MyAccountManager(BaseUserManager):
#   def create_user(self, email, username, password=None):
#     if not email:
#       raise ValueError("users must have emial")
#     if not username:
#       raise ValueError("users must have username")
#     user = self.model(
#       email=self.normalize_email(email),
#       username = username
#     )
#     user.set_password(password)
#     user.save(user = self._db)
#
#   def create_superuser(self, email, username, password):
#     user = self.model(
#       email=self.noramlize_email(email),
#       username=username,
#       password = password
#     )
#     user.is_admin = True
#     user.is_staff= True
#     user.is_superuser = True
#     user.save(using=self._db)
#
#
#
# class Account(AbstractBaseUser):
#   email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#   username = models.CharField(max_length=30, unique=True)
#   date_joined = models.DateTimeField(verbose_name="last joined", auto_now_add=True)
#   date_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
#   is_admin = models.BooleanField(default=False)
#   is_active = models.BooleanField(default=True)
#   is_staff = models.BooleanField(default=False)
#   is_superuser = models.BooleanField(default=False)
#   # first_name = models.CharField(ma)
#
#   USERNAME_FIELD = "email"
#   REQUIRED_FIELDS = ['username']
#
#   def __str__(self):
#     return self.email
#
#   objects = MyAccountManager()
#
#   def has_perm(self, perm, obj=None):
#     return self.is_admin
#
#   def has_module_perm(self, app_label):
#     return True





