from django.db import models

# step-4
from django.utils import timezone 
# step-12
from django.contrib.auth.models import User 

# Create your models here.
# step-1
class Post(models.Model):
    # step-7
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    # step-2
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length= 250)
    body = models.TextField()
    
    # step-13
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    
    # step-5 
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # step-8
    status = models.CharField(
        max_length=2, 
        choices=Status.choices, 
        default=Status.DRAFT
    )
    
    # step-6
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    # step-3        
    def __str__(self):
        return f"{self.title} - {self.slug} - {self.body}"
    

