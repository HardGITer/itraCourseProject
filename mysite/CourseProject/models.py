from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    name = models.CharField(max_length=50)
    shortDescription = models.TextField()
    specialityNumber = models.CharField(max_length=20)
    mainText = models.TextField()
    creationDate = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class LikeForArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starCount = models.IntegerField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    creationDate = models.DateTimeField()

class LikeForComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
    text = models.CharField(max_length=20)