from django.db import models


class Notification(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=255)
    time_set = models.DateTimeField(auto_now=True)





