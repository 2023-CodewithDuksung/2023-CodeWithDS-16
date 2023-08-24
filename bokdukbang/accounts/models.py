from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name=None, student_num=0, phone=None, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, name=name, student_num=student_num, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name=None, student_num=0, phone=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            name = name,
            student_num = student_num,
            password=password,
            phone = phone
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False)
    student_num = models.IntegerField(null=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    phone = models.CharField(max_length=45, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'student_num', 'phone']

    class Meta:
        managed = True
        db_table = 'user'

    def __str__(self):
        return f"({self.user_id}) {self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True