from django import forms
from django.forms import Textarea, TextInput

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        labels = {'title': 'Заголовок', 'text':'Текст', 'image':'Изображение'}
        widgets = {
            'text': Textarea(attrs={'class':"form-control", 'rows':'3', 'style':'resize:none'}),
            'title': TextInput(attrs={'class':"form-control", 'placeholder':"Заголовок"})
        }
