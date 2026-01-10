from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        "author": "John Doe",
        "title": "Blog post 1",
        "content": "Post content",
        "date_posted": "July 4, 1776",
    },
    {
        "author": "Jane Doe",
        "title": "Blog post 2",
        "content": "Post content",
        "date_posted": "July 4, 1776",
    },
]


def home(request):
    context = {"posts": posts, "title": "Home"}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
