from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profiles", verbose_name="Image", null=True, blank=True)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    link = models.URLField(verbose_name= "Link", null=True, blank=True)

    def __str__(self):
        return self.user