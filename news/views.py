from django.shortcuts import render
from .models import news
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

# Create your views here.
class BlogHomePage(ListView):
    model= news
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = news
    template_name = 'news_post_detail.html'

class BlogCreateView(CreateView):
    model = news
    template_name = 'post_new.html'
    fields = "__all__"

class BlogDeleteView(DeleteView):   
    model = news
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
    model = news
    template_name = 'post_update.html'
    fields =['title','author', 'message']   