from django.db import models

# Create your models here.


class example(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
