from django.db import models
from django.urls import reverse
from datetime import date, time
# from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    # snippet = models.CharField(max_length=200, default='Click Link Above To Read Post..')
    
    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.author
    
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    
class Comment(models.Model):
    post = models.ForeignKey("blog.post", on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text
    