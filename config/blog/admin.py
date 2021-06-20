from django.contrib import admin
from .models import Blog, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('name', 'email', 'is_active', 'is_staff')
    # フィールドをリンク化
    list_display_links = ('name', 'email')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_datetime',
                    'updated_datetime', 'author')
    list_display_links = ('title', 'text')


# 管理サイトに登録
admin.site.register(Blog, BlogAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
