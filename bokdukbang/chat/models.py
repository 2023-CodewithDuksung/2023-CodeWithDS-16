from django.db import models

# Create your models here.

class Messages(models.Model):
    messages_id = models.IntegerField(primary_key=True)
    chatroom = models.ForeignKey('Rooms', models.DO_NOTHING, blank=True, null=True)
    sender = models.ForeignKey('User', models.DO_NOTHING, db_column='sender', blank=True, null=True)
    content = models.TextField()
    sent_at = models.DateTimeField()
    isread = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'messages'
