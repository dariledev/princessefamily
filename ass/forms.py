from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from ass.models import PostArticle , QuesModel



class CreateUser(UserCreationForm):
    model = User
    fields = ['username' 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostArticle
        fields = '__all__'



class addQuestionform(forms.ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"









