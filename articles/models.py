from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug= models.SlugField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jfif', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title
    def snippet(self):
        return self.text[:50]+"..."
