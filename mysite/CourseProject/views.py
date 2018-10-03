import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, LikeForArticle, Comment, Rating

from django.utils.translation import ugettext as _


def index(request):
    # from django.utils import translation
    # user_language = 'ru'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    # .annotate(likes=Sum('likeforarticle__id')),
    #post = Article.objects.get(id=request.POST.get('id'))
    data = {"user": request.user, "articles": Article.objects.all(),
            "likesForArticles": LikeForArticle.objects.all(),
            "is_liked": True, "total_likes": 5, "rating": Rating.objects.all()}
    return render(request, 'CourseProject/index.html', context=data)


def cabinet(request, userid):
    if request.user.is_authenticated:
        articles = Article.objects.filter(user=userid)
        data = {"articles": articles}
        return render(request, "CourseProject/userPage.html", context=data)
    else:
        return redirect("/authentication/login")


def create(request, userid):
    if request.method == "POST":
        article = Article()
        article.name = request.POST.get("name")
        article.shortDescription = request.POST.get("shortDescription")
        article.specialityNumber = request.POST.get("specialityNumber")
        article.mainText = request.POST.get("editor")  # mainText
        article.creationDate = datetime.datetime.now()
        article.user = request.user
        article.save()
        # return redirect("main/cabinet")
        return render(request, "CourseProject/output.html", {"context": request.POST.get("editor")})
    else:
        return render(request, "CourseProject/create.html")


def edit(request, userid, id):
    try:
        article = Article.objects.get(id=id)
        if request.method == "POST":
            article.name = request.POST.get("name")
            article.shortDescription = request.POST.get("shortDescription")
            article.specialityNumber = request.POST.get("specialityNumber")
            article.mainText = request.POST.get("editor")
            article.save()
            redirecturl = '/main/cabinet/' + str(userid)
            return redirect(redirecturl)
        else:
            return render(request, "CourseProject/editArticle.html", {"article": article})
    except Article.DoesNotExist:
        return redirect("<h2>article does't found")


def delete(request, userid, id):
    redirecturl = '/main/cabinet/' + str(userid)
    try:
        article = Article.objects.get(id=id)
        if request.method == "GET":
            article.delete()
            return redirect(redirecturl)
        else:
            return redirect(redirecturl)
    except Article.DoesNotExist:
        return redirect("<h2>article does't found")


def output(request):
    return render(request, "CourseProject/output.html", {"context": request.POST.get("content")})


def view(request, id):
    try:
        article = Article.objects.get(id=id)
        # comments = Comment.objects.filter(article=article)
        is_liked = False
        if article.likes.filter(id=request.user.id).exists():
            is_liked = True
        else:
            is_liked = False
        return render(request, "CourseProject/viewArticle.html", {"article": article, "user": request.user,
            "is_liked": is_liked, "total_likes": article.likes.all().count()})
    except Article.DoesNotExist:
        return redirect("<h2>article does't found<h2>")
