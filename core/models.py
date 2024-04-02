from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/gallery')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Galleries'
        ordering = ['name']

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='comments')
    avatar = models.ImageField(upload_to='images/avatar/')
    occupation = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.user.username

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/icon')
    content = models.TextField()
    slug = models.SlugField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("service", args=[self.slug])
    
