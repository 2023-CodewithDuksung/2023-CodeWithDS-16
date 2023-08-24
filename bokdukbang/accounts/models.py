from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, student_num=0, phone=None, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, name=name, student_num=student_num, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, student_num=0, phone=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
            name=email,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser):
    username = models.CharField(max_length=40, null=False)
    student_num = models.IntegerField(null=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=45, null=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    phone = models.CharField(max_length=45, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['student_num', 'phone']

    class Meta:
        managed = True
        db_table = 'user'