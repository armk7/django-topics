from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField("Title", max_length=64, null=False, blank=False)


class Product(models.Model):
    title = models.CharField("Title", max_length=120)
    description = models.CharField("Description", max_length=240, default="")
    summary = models.CharField("Summary", max_length=160, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True)