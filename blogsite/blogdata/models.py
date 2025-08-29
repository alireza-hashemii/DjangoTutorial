from django.db import models
from extenstions.utils import jalali_converter
# Create your models here.
class Blog(models.Model):
    CHOICES = (
        ('d', 'draft'),
        ('p', 'published')
    )
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField('Tag',null=True,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media')
    status = models.CharField(choices=CHOICES, max_length=1)

    def __str__(self):
        return self.title
    
    def tags_published(self):
        return self.tags.filter(is_active=True)

    def persian_date(self):
        return jalali_converter(self.created_at)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.phone_number}"