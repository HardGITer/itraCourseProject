import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.template.loader import render_to_string

# from mysite.CourseProject.models import Article

from django.apps import apps
Article = apps.get_model('CourseProject', 'Article')
Comment = apps.get_model('CourseProject', 'Comment')
Rating = apps.get_model('CourseProject', 'Rating')

def index(request):
    return render(request,"test")

def like_post(request): # надо передавать все статьи, и как-то получать лайкнул юзер или нет
    post = Article.objects.get(id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.likes.all().count(),
        'article': post,
    }
    if request.is_ajax():
        html = render_to_string('feedback/like_section.html',context=context, request=request)
        return JsonResponse({'form': html})

def add_comment(request):
    article = Article.objects.get(id=request.POST.get("id"))

    comment = Comment()
    comment.article = article
    comment.user = request.user
    comment.text = request.POST.get('text')
    comment.creationDate = datetime.datetime.now()
    comment.save()
    commnets = Comment.objects.filter(article=article)

    context = {
        'comments': commnets,
        'article': article,
    }
    if request.is_ajax():
        html = render_to_string('feedback/comment_section.html',context=context, request=request)
        return JsonResponse({'form': html})

def check_comment(request):
    article = Article.objects.get(id=request.POST.get("id"))
    comments = Comment.objects.filter(article=article)
    context = {
        'comments': comments,
        'article': article,
    }
    if request.is_ajax():
        html = render_to_string('feedback/comment_section.html',context=context, request=request)
        return JsonResponse({'form': html})

def add_rating(request):
    article = Article.objects.get(id=request.POST.get("id"))
    # is_rated = False
    if Rating.objects.filter(user = request.user.id).exists():
        # is_rated = False
        rating = Rating.objects.get(user = request.user.id)
        rating.starCount = request.POST.get('starCount')
        rating.save()
    else:
        rating = Rating()
        rating.article = article
        rating.user = request.user
        rating.starCount = request.POST.get('starCount')
        rating.save()
        # is_rated = True

    context = {
        'article': article,
        # 'is_rated': is_rated,
    }
    if request.is_ajax():
        html = render_to_string('feedback/rating_section.html', context=context, request=request)
        return JsonResponse({'form': html})
