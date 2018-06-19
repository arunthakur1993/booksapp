# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    first_name = models.CharField(max_length =100)
    last_name  = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s'%(self.first_name,self.last_name)

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length =200)
    city =models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length = 100)
    overview = models.CharField(max_length = 300)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
