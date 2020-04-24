from django.urls import include,path

from .views import blog_list,blog_retrieve

app_name = 'auth'
urlpatterns = (
    path('', blog_list, name="blog_list"),
    path('<int:pk>/', blog_retrieve, name="blog_retrieve"),
)