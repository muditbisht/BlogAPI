
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from api.authentication.forms import RegisterationForm, LoginForm


# Create your views here.



class Login(APIView):

    def post(self, request):
        login_form = LoginForm(request.POST)
        context = {}
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            if user and user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                context['valid'] = True
                context['token'] = token.key
                context['errors'] = login_form.errors
            else:
                context['valid'] = False
                context['errors'] = "Invalid Username or Password."
        else:
            context['valid'] = False
        return Response(context)


auth_login = Login.as_view()


class Register(APIView):

    def post(self, request):
        print(dir(request))
        register_form = RegisterationForm(request.POST)
        context = {}
        if register_form.is_valid():
            context['valid'] = True
            user = register_form.get_user()
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            print(dir(token))
            context['token'] = token.key
        else:
            context['valid'] = False
        context['errors'] = register_form.errors
        return Response(context)


auth_registeration = Register.as_view()


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.POST, request.headers)
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'Logged Out':'Success'})

auth_logout = Logout.as_view()

