from django.db import models
from rooms_posts.models import Rooms
from accounts.models import User

# Create your models here.

class Messages(models.Model):
    messages_id = models.AutoField(primary_key=True)
    chatroom = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField()
    isread = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'messages'
