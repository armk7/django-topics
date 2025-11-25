from django.db import models
import uuid

# Create your models here.

class Collection(models.Model):
    title = models.CharField("Title", max_length=128, null=False, blank=False)

class Category(models.Model):
    title = models.CharField("Title", max_length=64, null=False, blank=False)


class Product(models.Model):
    title = models.CharField("Title", max_length=120)
    description = models.CharField("Description", max_length=240, default="")
    summary = models.CharField("Summary", max_length=160, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    uuid = models.UUIDField("UUID", primary_key=True, default=uuid.uuid4, editable=False, null=False)