from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class poll():

    title = models.CharField(max_length=100)
    def str(self):
        return self.title