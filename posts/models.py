from django.db import models
from django.contrib.auth.models import User
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
    title = models.CharField(max_length=100, name="title")
    description = models.TextField(name="description")
    img = models.ImageField(upload_to= "posts", verbose_name="img")
    link = models.URLField(verbose_name = "link")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="category")#porque un post puede pertenecer a muchas categorías y viceversa
    created = models.DateTimeField(auto_now_add= True, verbose_name="created")
    updated = models.DateField(auto_now=True, verbose_name= "updated")

    class Meta():
        ordering = ["-updated"]

    def __str__(self):
        return self.title
