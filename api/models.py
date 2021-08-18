from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

# Create your models here.
class Porfolio(models.Model):
    number              = models.IntegerField(default=1)
    image_project       = models.ImageField(upload_to="static/img/porfolio")
    name_project        = models.CharField(max_length=25, default="")
    short_description   = models.CharField(max_length=100, default="")
    long_description    = RichTextField(default="")
    source_code         = models.URLField(default="")
    technologies        = models.TextField(default="")

    def __str__(self):
        return self.name_project

class Blogs(models.Model):
    title                   = models.CharField(max_length=53, default="")
    slug                    = AutoSlugField(populate_from='title')
    image_blog              = models.ImageField(upload_to='static/img/blog')
    short_blog_description  = models.CharField(max_length=320, default="")
    long_blog_description   = RichTextField(default="")
    publish_date            = models.DateTimeField(auto_now_add=True)
    author                  = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title