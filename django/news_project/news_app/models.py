from django.db import models
from django.utils import timezone

# Create your models here.
class PublishedManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
  name = models.CharField(max_length=150)

  def __str__(self):
    return self.name

class News(models.Model):
  class Status(models.TextChoices):
    Draft = "DF", "Draft"
    Published = "PB", "Published"

  # id = models.IntegerField(primary_key=True, unique=True)
  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250)
  body = models.TextField()
  image = models.ImageField(upload_to='news/images') #Rasmlar bilan ishlaganda "pillow" kutubxonasini o'rnatish kerak bo'ladi.
  # pipenv install Pillow
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  publish_time = models.DateTimeField(default=timezone.now)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

  objects = models.Manager()
  published = PublishedManager()

  class Meta:
    ordering = ["-publish_time"]

  def __str__(self):
    return self.title
