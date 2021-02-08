from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class BlogCategory(models.Model):
    title = models.CharField(max_length = 20)
    slug  = models.SlugField(max_length = 20, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("category",kwargs={'slug':self.title})
        
            


class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE,null=True,related_name="BlogPost")
    date  = models.DateTimeField(auto_now_add = True)
    body = models.TextField(max_length = 350, null= True)
    title = models.CharField(max_length = 100)
    slug = models.SlugField(null=True)
    status_choices  = [
        ("PUB","published"),
        ("DRA", "draft")

    ]
    status = models.CharField(max_length = 12,choices = status_choices, default = "draft")
    category = models.ForeignKey(BlogCategory,on_delete = models.CASCADE,null= True,related_name = "blog_post")
    def __str__(self):
        return self.title
        class Meta:
            ordering = ("date")
    def get_absolute_url(self):
        return f"category/new/{self.slug}"
