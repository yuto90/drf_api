from django.urls import path, include
from blog import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Viewでquerysetの記述があればbasenameの設定はいらない
# api/profileに来たら発火
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<str:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('', include(router.urls)),  # routeに接続
]
