from django.contrib import admin
from blog import models

# Register your models here.

# UserProfileを管理画面に登録
admin.site.register(models.UserProfile)
admin.site.register(models.Blog)
