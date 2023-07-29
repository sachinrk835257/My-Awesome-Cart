from django.db import models

# Create your models here.
class blogPost(models.Model):
    blog_id = models.AutoField(primary_key=True)
    h1 = models.CharField(max_length=100,default="related to which area")
    h2 = models.CharField(max_length=100,default="title of blog post")
    publish_date = models.DateTimeField(auto_now_add=True)
    p2 = models.CharField(max_length=1000,default="description")
    thumbnail = models.ImageField(upload_to='blog/images',default="upload image")

    def __str__(self):
        return self.h1
