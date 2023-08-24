from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    student_num = models.PositiveIntegerField()
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    last_login = models.DateTimeField()
    phone = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'