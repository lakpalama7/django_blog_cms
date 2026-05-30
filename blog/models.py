from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=256)
    message = models.TextField()
    message_sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"

    def __str__(self):
        return f'Message from {self.name} - {self.email}'
    

