from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Poll():
#     title = models.CharField(max_length=100)
#     upvotes = models.IntegerField()
#     downvotes = models.IntegerField()
#     def str(self):
#         return self.title