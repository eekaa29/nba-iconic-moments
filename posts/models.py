from django.db import models
from django.contrib.auth.models import User
from franchise.models import Franchise
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")
    created = models.DateTimeField(auto_now_add= True, verbose_name="created")
    updated = models.DateField(auto_now=True, verbose_name= "updated")

    class Meta():
        verbose_name_plural = "categories"
        ordering = ["created"]
    def __str__(self):
        return self.name
    

class Post(models.Model):
    franchise = models.ForeignKey(Franchise, default= None, verbose_name="Franchise", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Title", null=True, blank=True)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    img = models.ImageField(upload_to= "posts", verbose_name="Img", blank=True, null=True)
    link = models.URLField(verbose_name = "link", blank=True)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories", blank=True)#porque un post puede pertenecer a muchas categorías y viceversa
    created = models.DateTimeField(auto_now_add= True, verbose_name="Created")
    updated = models.DateField(auto_now=True, verbose_name= "Updated")

    class Meta():
        ordering = ["-updated"]

    def __str__(self):
        return self.title
