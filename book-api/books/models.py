from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title