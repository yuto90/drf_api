from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    created_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Blog
        # modelで設定したカラム名
        fields = ('id', 'text', 'created_datetime', 'updated_datetime')
