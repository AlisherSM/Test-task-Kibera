from django import forms
from .models import News


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'news_text', 'author']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "news_text": forms.Textarea(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
        }
