from django.db import models

# Create your models here.
class Puzzle(models.Model):
    name=models.CharField(max_length=200)
    pieces=models.IntegerField()