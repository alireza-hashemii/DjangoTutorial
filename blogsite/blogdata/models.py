from django.db import models

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

class Tag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title