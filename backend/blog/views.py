from django.shortcuts import render

# restframeworkでは、値を返す際にResponseを用いる
from rest_framework.response import Response

# Viewsetsを継承してクラスベースビューを作成
from rest_framework import viewsets

# シリアライザーをimport
from profiles_api import serializers

# Create your views here.


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses action (list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})
