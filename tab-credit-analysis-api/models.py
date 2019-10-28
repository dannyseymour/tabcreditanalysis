from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60)
    ##TODO: add rest of data points

    def __str___(self):
        return self.name
# Create your models here.
