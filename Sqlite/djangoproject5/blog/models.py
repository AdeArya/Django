from django.db import models
from django.shortcuts import reverse

class Article(models.Model):
    title   = models.CharField(max_length=255)
    body    = models.TextField()
    creator = models.CharField(max_length=255)
    publish = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}.{}".format(self.id, self.title)
    
    def get_absolute_url(self):
        return reverse('blog:list')