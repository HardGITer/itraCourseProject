import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article

from django.utils.translation import ugettext as _

def index(request):
    data = {"user":request.user.id}
    return render(request, 'CourseProject/index.html', context=data)

def cabinet(request):
    articles = Article.objects.all()
    data = {"articles": articles}
    return render(request, "CourseProject/userPage.html", context=data)

def createArticle(request):
    if request.method == "POST":
        article = Article()
        article.name = request.POST.get("name")
        article.shortDescription = request.POST.get("shortDescription")
        article.specialityNumber = request.POST.get("specialityNumber")
        article.mainText = request.POST.get("mainText")
        article.creationDate = datetime.datetime.now()
        article.user = request.user
        article.save()
    return redirect("/main/cabinet/")