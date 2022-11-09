from django.urls import path
from .views import BlogDetailView, BlogHomePage, BlogCreateView, BlogDeleteView, BlogUpdateView


urlpatterns = [
    path('', BlogHomePage.as_view(), name='home'),
    path('news/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('news/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_update'),
    path('news/<int:pk>/', BlogDetailView.as_view(), name='news_post_detail'),
    path('news/new/', BlogCreateView.as_view(), name='post_new'),
]
