from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    language=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    image=models.ImageField(upload_to="book-image",null=True)

    def __str__(self):
        return self.title