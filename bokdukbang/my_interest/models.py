from django.db import models

# Create your models here.
class MyInterest(models.Model):
    interest_id = models.IntegerField(primary_key=True)
    muser = models.ForeignKey('User', models.DO_NOTHING)
    studio = models.ForeignKey('Rooms', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_interest'