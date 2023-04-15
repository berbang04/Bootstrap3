from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Person(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatar')
    instagram = models.CharField(max_length=30)
    slug=models.SlugField(max_length=200)


# Create your models here.
