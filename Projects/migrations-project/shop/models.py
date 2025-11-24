from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField("Title", max_length=120)
    description = models.CharField("Description", max_length=240, default="")
    summary = models.CharField("Summary", max_length=160, default="")