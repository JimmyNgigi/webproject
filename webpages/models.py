from django.db import models

# Create your models here.
class Myuser(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Age = models.IntegerField(null=True, blank=False)

