from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
# from Search.search import ArticleIndex


class Article(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    shortDescription = models.TextField(blank=True, null=True)
    specialityNumber = models.CharField(max_length=20, blank=True, null=True)
    mainText = models.TextField(blank=True, null=True)
    creationDate = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def get_rating_for_article(self):
        return self.rating_set.filter(article_id=self.id).aggregate(Avg('starCount'))

    def indexing(self):
        from Search.search import ArticleIndex
        obj = ArticleIndex(
            meta={'id': self.id},
            mainText=self.mainText,
            shortDescription=self.shortDescription,
            name=self.name,
            specialityNumber=self.specialityNumber
        )
        obj.save()
        return obj.to_dict(include_meta=True)
    # def indexing(self):
    #     from Search.search import ArticleIndex
    #     obj = ArticleIndex(meta={'id': self.id}, name=self.name, creationDate=self.creationDate,
    #                        shortDescription=self.shortDescription, specialityNumber=self.specialityNumber)
    #     return obj.to_dict(include_meta=True)

class Tag(models.Model):
    text = models.CharField(max_length=20)
    article = models.ManyToManyField(Article)

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

    def get_likes_for_comment(self):
        return self.likeforcomment_set.filter(comment_id=self.id).count()

class LikeForComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)