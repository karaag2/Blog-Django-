from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()


class BlogPost (models.Model) :
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models. TextField(blank=True)
    description = models.TextField()
    # @property
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # type: ignore
            super().save(*args, **kwargs)