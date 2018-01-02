from django.shortcuts import render, redirect

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


def post(request, post):
    this_post = Post.objects.get(id=post)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post.html', {'post': this_post, 'comments': comments})


def create(request):
    pass


def comment(request):
    success = False
    post = Post.objects.get(id=request.POST.get('post'))
    comments = Comment.objects.filter(post=post)
    try:

        success = Comment.objects.create(post=post,
                                        reply=request.POST.get('comment'),
                                        creator=request.user)
        success.save()
    finally:
        return redirect('forum', post.id)
