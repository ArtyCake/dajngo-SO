from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
  title =models.CharField(max_length=200)
  content = models.TextField()
  user = models.ForeignKey(User)
  create_date = models.DateTimeField()

class Comments(models.Model):
  question = models.ForeignKey(Questions)
  content = models.TextField()
  user = models.ForeignKey(User)
  create_date = models.DateTimeField()

