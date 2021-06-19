from django.contrib import admin
from .models import Blog, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('name', 'email', 'is_active', 'is_staff')
    list_display_links = ('name', 'email')


class BlogAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('title', 'text', 'created_datetime',
                    'updated_datetime', 'author')
    list_display_links = ('title', 'text')


admin.site.register(Blog, BlogAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
