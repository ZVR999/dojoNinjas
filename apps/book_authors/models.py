# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(1000)
    created_at = models.DateTime(auto_now_add=True)
    updated_at = models.DateTime(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToMany(Book, related_name='Authors')
    email = models.CharField(max_length=255)
    created_at = models.DateTime(auto_now_add=True)
    updated_at = models.DateTime(auto_now = True)
    