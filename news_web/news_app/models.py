from django.db import models

# Create your models here.

class Article(models.Model):
    CHOICES = (
        ('p', 'published'),
        ('d', 'draft'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=CHOICES, max_length=1)
