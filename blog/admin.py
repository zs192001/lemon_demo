from django.contrib import admin

from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['blog_tile', 'blog_text']

admin.site.register(BlogPost, BlogPostAdmin)
