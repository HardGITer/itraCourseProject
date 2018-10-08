from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render
from django.views.generic import FormView


from django.views.generic.edit import FormView

from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "authentication/login.html"
    success_url = "/main"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "authentication/register.html"

    def form_valid(self, form):
        return form.save()

def logoutView(request):
    logout(request)
    from CourseProject.models import Article, LikeForArticle, Rating
    data = {"user": request.user, "articles": Article.objects.all(),
            "likesForArticles": LikeForArticle.objects.all(),
            "is_liked": True, "total_likes": 5, "rating": Rating.objects.all()}
    return render(request, 'CourseProject/index.html', context=data)
