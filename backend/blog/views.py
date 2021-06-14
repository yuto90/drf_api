from blog import serializers
from rest_framework import generics
from .models import Blog


# Create your views here.

# LIstAPIView GET 一覧取得
class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer


# RetrieveAPIView GET 取得
class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
