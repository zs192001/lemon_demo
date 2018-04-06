from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import BlogPost

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'
    
    def get_queryset(self):
        return BlogPost.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    
    #def get_queryset(self):
        #return BlogPost.objects.filter(pub_date__lte=timezone.now())

