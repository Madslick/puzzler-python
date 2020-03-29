from django.db import models
from .theme import Theme

# Create your models here.
class Puzzle(models.Model):
    name=models.CharField(max_length=200)
    pieces=models.IntegerField()
    themes=models.ManyToManyField(Theme)