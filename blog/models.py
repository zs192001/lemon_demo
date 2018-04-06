from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class BlogPost(models.Model):
    blog_title = models.CharField(max_length = 200)
    blog_text = RichTextUploadingField('contents')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.blog_title
