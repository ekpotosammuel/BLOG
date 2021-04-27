from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Comment
from django.urls import reverse_lazy







# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    ordering=['-id','-post_date']
    # ordering=['-post_date']
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context
    
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
class AboutPageView(TemplateView): 
    template_name = 'about.html'

class CommentCreateView(CreateView):
    model = Post
    template_name = 'comment.html'
    fields = ['author', 'body']

    