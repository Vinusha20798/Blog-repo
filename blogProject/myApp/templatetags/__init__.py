from django import template
from myApp.models import Post
register=template.Library() #default template tag is total_post
@register.simple_tag
def total_posts():
   return Post.objects.count()