from django.shortcuts import render
from .models import Post, Author
# Create your views here.
def  main_page(request):
    return render(request, "main_page.html")


def post_view(request):
    posts = Post.objects.filter(published = True)
    return render(request, "posts_page.html", {"posts": posts})