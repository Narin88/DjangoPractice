from django import forms
from django.forms import ModelForm

from .models import Article, Project

class ArticleCreationForm(ModelForm):
  # content field가 만들어질때 먼저설정하는 class style
  content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left', 'style': 'height: auto;'}))

  project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

  class Meta:
    model = Article
    fields = ['title', 'image', 'project', 'content']