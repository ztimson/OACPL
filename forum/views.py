from django.shortcuts import render, redirect

from .forms import CommentForm, CreatePostForm, EditPostForm
from .models import Thread, Post, Comment


def view(request, thread=None):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('post', post=instance.id)
    else:
        form = CreatePostForm()

    my_posts = None
    if request.user.is_authenticated():
        my_posts = Post.objects.filter(creator=request.user, resolved=False)
    if not thread:
        threads = Thread.objects.all()
        thread_name = None
        posts = Post.objects.filter(resolved=False).order_by('-created')[:10]
    else:
        threads = None
        thread_name = Thread.objects.get(id=thread).topic
        posts = Post.objects.filter(topic=thread).order_by('-created')
    return render(request, 'view.html', {'threads': threads, 'posts': posts, 'myPosts': my_posts, 'thread': thread_name, 'form': form})


def viewPost(request, post):
    this_post = Post.objects.get(id=post)

    if request.method == 'POST':
        if request.POST.get('request') == 'comment':
            form = CommentForm(request.POST)
            Comment.objects.create(post_id=post,
                                   reply=form.data.get('reply'),
                                   creator=request.user)
        elif request.POST.get('request') == 'edit':
            form = EditPostForm(request.POST, instance=this_post)
            form.save()
        elif request.POST.get('request') == 'resolve':
            if this_post.creator == request.user or request.user.has_perm('forum.change_post'):
                this_post.resolved = True
                this_post.save()
        elif request.POST.get('request') == 'delete':
            if this_post.creator == request.user or request.user.has_perm('forum.delete_post'):
                this_post.delete()
                return redirect('forum')

    form = CommentForm()
    edit_form = EditPostForm(instance=this_post)
    comments = Comment.objects.filter(post=this_post)
    return render(request, 'post.html', {'post': this_post, 'comments': comments, 'form': form, 'editForm': edit_form})
