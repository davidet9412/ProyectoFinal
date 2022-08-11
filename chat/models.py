from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    text = models.CharField(max_length=256)
    origin = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="origin")
    target = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="target")
    timestamp = models.DateTimeField(auto_now=True)