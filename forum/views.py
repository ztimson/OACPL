from django.shortcuts import render

from .models import Thread, Post, Comment


def view(request, thread=None):
    myPosts = None
    if request.user.is_authenticated():
        myPosts = Post.objects.filter(creator=request.user)
    if not thread:
        threads = Thread.objects.all()
        posts = Post.objects.order_by('created')[:10]
    else:
        threads = None
        posts = Post.objects.filter(topic=thread)
    return render(request, 'view.html', {'threads': threads, 'posts': posts, 'myPosts': myPosts})


def post(request):
    pass


def create(request):
    pass


def comment(request):
    pass
