from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='dev-home'),
    path('articles', ArticleListView.as_view(), name='dev-articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new', ArticleCreateView.as_view(), name='articles-create'),
    path('articles/<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete'),
    path('books', BookListView.as_view(), name='dev-books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new', BookCreateView.as_view(), name='books-create'),
    path('books/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
    path('videos', VideoListView.as_view(), name='dev-videos'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('videos/new', VideoCreateView.as_view(), name='videos-create'),
    path('videos/<int:pk>/update', VideoUpdateView.as_view(), name='video-update'),
    path('videos/<int:pk>/delete', VideoDeleteView.as_view(), name='video-delete'),
]