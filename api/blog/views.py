from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


from .models import Blog
from .serializers import BlogSerializer
from .forms import BlogForm

# Create your views here.
class BlogList(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self,request):
        serializer = self.serializer_class(Blog.objects.all(),many=True)
        return Response(serializer.data)

    def post(self,request):
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            title = blog_form.cleaned_data['title']
            content = blog_form.cleaned_data['content']
            blog = Blog(title=title, content=content, author=request.user)
            blog.save()
            return Response({'valid':True, 'blog_ID':blog.id})
        else:
            return Response({'valid':False,'errors':blog_form.errors})


blog_list = BlogList.as_view()


class BlogRetrieve(RetrieveAPIView):
    permission_classes =  [IsAuthenticated]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

blog_retrieve = BlogRetrieve.as_view()
