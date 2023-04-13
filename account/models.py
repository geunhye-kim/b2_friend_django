from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
