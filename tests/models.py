from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField(null=True)

class Course(models.Model):
    start_at = models.DateTimeField()
    duration = models.DateTimeField()

class BookTest(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField()
    slug = models.SlugField(null=True)
    slug1 = models.SlugField(null=True)

