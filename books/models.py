from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str___(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)