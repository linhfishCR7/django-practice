from django.db import models

# Create your models here.

class Program(models.Model):
    name = models.CharField(
        max_length=20,
    )


class Price(models.Model):
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE
    )
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    amount = models.IntegerField()


class Order(models.Model):
    state = models.CharField(
        max_length=20,
    )
    items = models.ManyToManyField(Price)


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
