from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'

class Category(models.Model):

    title = models.CharField('Название категории', max_length=100)

    def __str__(self):
        return f'{self.title}'

class Post(models.Model):

    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Картинка')
    description = models.TextField('Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField('Дата', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'