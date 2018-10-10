import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from CourseProject.forms import ArticleCreateForm, UserEditForm
from .models import Article, LikeForArticle, Comment, Rating, Tag
# from Search.documents import ArticleDocument
from django.utils.translation import ugettext as _


def index(request):
    # from django.utils import translation
    # user_language = 'ru'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    # .annotate(likes=Sum('likeforarticle__id')),
    #post = Article.objects.get(id=request.POST.get('id'))
    print(request.user.is_superuser)
    data = {"user": request.user, "articles": Article.objects.all(),
            "likesForArticles": LikeForArticle.objects.all(),
            "is_liked": True, "total_likes": 5, "rating": Rating.objects.all()}
    return render(request, 'CourseProject/index.html', context=data)

def absoluteSearch(request):
    q = request.GET.get('q')
    articles = ''
    if q:
        articles = ArticleDocument.search().query("match", title=q)
    else:
        posts = ''

    return render(request, 'search/search.html', {"articles": articles})

@login_required(login_url="login")
def cabinet(request, userid):
    if request.user.is_authenticated:
        articles = Article.objects.filter(user=userid)
        data = {"articles": articles, "form": UserEditForm()}
        return render(request, "CourseProject/userPage.html", context=data)
    else:
        return redirect("/authentication/login")

@login_required(login_url="login")
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
        print(request.POST.get("tags").split(','))
        tagsArr = request.POST.get("tags").split(',')
        for i in tagsArr:
            currTag = Tag.objects.filter(text=i)
            if currTag.exists():
                # tag = Tag()
                # tag.text = i
                # tag.save()
                article.tag_set.add(Tag.objects.get(text=i))
                # tag.save()
            else:
                tag = Tag()
                tag.text = i
                tag.save()
                article.tag_set.add(tag)
                tag.save()
        # return redirect("main/cabinet")
        return render(request, "CourseProject/output.html", {"context": request.POST.get("editor")})
    else:
        return render(request, "CourseProject/create.html")

@login_required(login_url="login")
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

@staff_member_required(login_url="login")
def adminEdit(request, id):
    try:
        article = Article.objects.get(id=id)
        if request.method == "POST" :
            article.name = request.POST.get("name")
            article.shortDescription = request.POST.get("shortDescription")
            article.specialityNumber = request.POST.get("specialityNumber")
            article.mainText = request.POST.get("editor")
            article.save()
            redirecturl = '/main/adminEdit/' + str(id)
            return redirect(redirecturl)
        else:
            return render(request, "CourseProject/editArticle.html", {"article": article})
    except Article.DoesNotExist:
        return redirect("<h2>article does't found")

@login_required(login_url="login")
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

@login_required(login_url="login")
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

def editUser(request):
    if request.method == "POST":
        form = UserEditForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserEditForm(instance=request.user)
    articles = Article.objects.filter(user=request.user)
    data = {"articles": articles, 'form':form}
    return render(request, "CourseProject/userPage.html", context=data)
