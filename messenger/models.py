from django.db import models

class Message(models.Model):
    subject = models.CharField(max_length=50, blank=False)
    body = models.CharField(max_length=200, blank=False)
    sender = models.ForeignKey('auth.User', blank=False, related_name="messages_sent")
    recipient = models.ForeignKey('auth.User', blank=False, related_name="messages_received")
    read = models.BooleanField(default=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject