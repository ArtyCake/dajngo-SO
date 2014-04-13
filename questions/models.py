# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
  title =models.CharField(max_length=200, verbose_name=u"Заголовок")
  content = models.TextField(verbose_name=u"Вопрос подробно")
  user = models.ForeignKey(User)
  create_date = models.DateTimeField()

class Comments(models.Model):
  question = models.ForeignKey(Questions)
  content = models.TextField(verbose_name=u"Комментарий")
  user = models.ForeignKey(User)
  create_date = models.DateTimeField()

