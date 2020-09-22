from django.db import models

class Market(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    swap = models.CharField(max_length=100)
    price = models.IntegerField()
    content = models.TextField()
    file_route = models.CharField(max_length=100)
    tag = models.CharField(max_length=200)

