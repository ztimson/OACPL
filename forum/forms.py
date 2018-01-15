from django import forms

from tinymce import TinyMCE

from .models import Comment, Post, Thread


class CommentForm(forms.ModelForm):
    reply = forms.CharField(widget=TinyMCE(mce_attrs={'height': 200}))

    class Meta:
        model = Comment
        fields = ['reply']


class CreatePostForm(forms.ModelForm):
    question = forms.CharField(widget=TinyMCE(mce_attrs={'height': 200}))

    class Meta:
        model = Post
        fields = ['title', 'thread', 'question']


class EditPostForm(forms.ModelForm):
    question = forms.CharField(widget=TinyMCE(mce_attrs={'height': 200}))

    class Meta:
        model = Post
        fields = ['question']
