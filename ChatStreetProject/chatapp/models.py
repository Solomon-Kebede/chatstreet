from django.db import models

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    last_seen = models.DateTimeField(blank=True, null=True)
    last_message_sent = models.CharField(max_length=1000000000000)
    profile_picture = models.ImageField(upload_to='profile_pic', null=True)

    def __str__(self):
        return self.name