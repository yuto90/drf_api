from blog import serializers
from rest_framework import generics
from .models import Blog, UserProfile
from rest_framework import viewsets


# Create your views here.

# LIstAPIView GET 一覧取得
class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer


# RetrieveAPIView GET 取得
class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer


# ModelViewSet　自前でCRUD処理を実装してくれる
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
