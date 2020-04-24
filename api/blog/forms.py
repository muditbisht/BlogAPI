from django import forms
from django.contrib.auth.models import User
class BlogForm(forms.Form):
    title = forms.CharField(min_length="5", required=True)
    content = forms.CharField(required=True)
