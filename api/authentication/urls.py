from django.urls import include,path

from api.authentication.views import auth_login,auth_logout,auth_registeration

app_name = 'authentication'
urlpatterns = (
    path('register/', auth_registeration),
    path('login/', auth_login),
    path('logout/', auth_logout),
)