from __future__ import unicode_literals
from django.db import models
from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=200)
    mainPicture = models.ImageField()
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    mainPicture = models.ImageField()
    text = models.CharField(max_length=10000)
    pup_date = models.DateField()
    section = models.ForeignKey(Section)
    def __str__(self):
        return self.title
class Tag(models.Model):
    text = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)
    def __str__(self):
        return self.text

#class Comment(models.Model):
 #   text = models.CharField(max_length=1000)
  #  username = models.CharField(max_length=50)
   # com_date = models.DateField()
    #post = models.ForeignKey(Post)
   # def __str__(self):
  #      return self.text
#class Reply(models.Model):












