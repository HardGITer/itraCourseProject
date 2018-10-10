from django import forms
from django.contrib.auth.models import User

from CourseProject.models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'name',
            'shortDescription',
            'specialityNumber',
            'mainText',

        )

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )