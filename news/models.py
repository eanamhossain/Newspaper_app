from email import message
from turtle import title
from django.db import models
from django.urls import reverse
# Create your models here.

class news(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news_post_detail", kwargs={"pk": self.pk})
    