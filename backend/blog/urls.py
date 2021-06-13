from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<str:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
