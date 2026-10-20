from django.contrib.auth.models import User
from django.db import models 

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Name")

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'  
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title