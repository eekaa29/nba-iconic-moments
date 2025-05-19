from django.db import models
from django.utils.text import slugify
# Create your models here.

class Franchise(models.Model):
    conference = models.CharField(max_length=100, verbose_name="conference")
    name = models.CharField(max_length=100, verbose_name="name")
    city = models.CharField(max_length=100, verbose_name="city")
    link = models.URLField(null=True, blank=True, verbose_name="link")
    img = models.ImageField(upload_to="franchise", verbose_name="img", null=True)

    
    class Meta:
        ordering = ["conference"]


    def __str__(self):
        return self.name
