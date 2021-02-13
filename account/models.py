from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, city, address, phone_number, password=None):
        if not email:
            raise ValueError("This is required field")
        if not first_name:
            raise ValueError("This is required field")
        if not last_name:
            raise ValueError("This is required field")
        if not username:
            raise ValueError("This is required field")
        if not city:
            raise ValueError("This is required field")
        if not address:
            raise ValueError("This is required field")
        if not phone_number:
            raise ValueError("This is required field")

        user = self.model(
                email           = self.normalize_email(email),
                first_name      = first_name,
                last_name       = last_name,
                username        = username,
                city            = city.capitalize(),
                address         = address,
                phone_number    = phone_number,
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, password, city, address, phone_number):
        user = self.create_user(
                email           = self.normalize_email(email),
                first_name      = first_name,
                last_name       = last_name,
                username        = username,
                password        = password,
                city            = city.capitalize(),
                address         = address,
                phone_number    = phone_number,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    user_id         = models.AutoField(primary_key=True)
    first_name 		= models.CharField(max_length=20) 
    last_name 		= models.CharField(max_length=20)
    email           = models.EmailField(verbose_name="email", unique=True)
    username 		= models.CharField(max_length=30, unique=True)
    city            = models.CharField(max_length=15)
    address         = models.TextField()
    phone_number    = models.CharField(max_length=12, unique=True)
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "password", "city", "address", "phone_number"]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True