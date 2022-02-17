from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import *


# Create your views here.

def home(request):
    return render(request, 'dev_templates/home.html')


class ArticleListView(ListView):
    model = Articles
    template_name = 'dev_templates/articles.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 2


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'dev_templates/article_detail.html'


class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'dev_templates/article_form.html'
    fields = ['title', 'brief', 'link', 'author']


class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'dev_templates/article_form.html'
    fields = ['title', 'brief', 'link', 'author']


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'dev_templates/article_confirm_delete.html'
    success_url = '/tools'


class BookListView(ListView):
    model = Books
    template_name = 'dev_templates/books.html'
    context_object_name = 'books'
    ordering = ['-date_posted']


class BookDetailView(DetailView):
    model = Books
    template_name = 'dev_templates/book_detail.html'


class BookCreateView(CreateView):
    model = Books
    template_name = 'dev_templates/book_form.html'
    fields = ['title', 'brief', 'file', 'author']


class BookUpdateView(UpdateView):
    model = Books
    template_name = 'dev_templates/book_form.html'
    fields = ['title', 'brief', 'file', 'author']


class BookDeleteView(DeleteView):
    model = Books
    template_name = 'dev_templates/book_confirm_delete.html'
    success_url = '/tools'


class VideoListView(ListView):
    model = Videos
    template_name = 'dev_templates/videos.html'
    context_object_name = 'videos'
    ordering = ['-date_posted']


class VideoDetailView(DetailView):
    model = Videos
    template_name = 'dev_templates/video_detail.html'


class VideoCreateView(CreateView):
    model = Videos
    template_name = 'dev_templates/video_form.html'
    fields = ['title', 'brief', 'link', 'channel']


class VideoUpdateView(UpdateView):
    model = Videos
    template_name = 'dev_templates/video_form.html'
    fields = ['title', 'brief', 'link', 'channel']


class VideoDeleteView(DeleteView):
    model = Videos
    template_name = 'dev_templates/video_confirm-delete.html'
    success_url = '/tools'
