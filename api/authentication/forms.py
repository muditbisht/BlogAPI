from django import forms
from django.forms import Form
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import re


class LoginForm(Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
            return user.username
        except User.DoesNotExist:
            raise ValidationError('Invalid Username or Password.')

class RegisterationForm:

    def __init__(self, data):
        self.data = data
        self.errors = {'username':[], 'password':[]}
        self.cleaned_data = {}
    def clean_username(self):
        username = self.data['username']
        print(username)
        if not re.compile(r'^[a-z_]\w+').match(username):
            raise ValidationError('Username should be in all lower_case with underscore (_) and digits.')
        if User.objects.filter(username=username).count()>0:
            raise ValidationError('Username already exists.')
        return username

    def get_user(self):
        user = User(username=self.cleaned_data['username'])
        user.set_password(self.cleaned_data['password'])
        return user

    def clean_password(self):
        password = self.data['password']
        print(password)
        if len(password) > 6:
            return password
        else:
            raise ValidationError('Password length must be greater than 6')


    def is_valid(self):
        err = False
        if not 'username' in self.data:
            self.errors['username'].append('required')
            err = True
        if not 'password' in self.data:
            self.errors['password'].append('required')
            err = True
        if err:
            return False
        try:
            self.cleaned_data['username'] = self.clean_username()
        except ValidationError as V:
            self.errors['username'].append(V.message)
            return False

        try:
            self.cleaned_data['password'] = self.clean_password()
        except ValidationError as V:
            self.errors['password'].append(V.message)
            return False

        return True