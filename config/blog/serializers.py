from rest_framework import serializers
from .models import Blog, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        # Serializersに紐付けるmodelを定義
        model = UserProfile
        # APIとして出力したいカラムを定義（タプル形式）
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                # セキュリティの関係上パスワードは書き込むだけ。
                'write_only': True,
                # パスワード入力の際に「・・・」となるようにstyleを指定
                'style': {'input_type': 'password'}
            }
        }

    # ModelSerializerにデフォルトでcreate(),update()が実装されているが
    # passwordがハッシュ化されないので、それぞれオーバーライドする
    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)


class BlogSerializer(serializers.ModelSerializer):
    created_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    updated_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    # authorのserializerを上書き
    author = UserProfileSerializer()

    class Meta:
        model = Blog
        fields = ('id', 'text', 'created_datetime',
                  'updated_datetime', 'author')
