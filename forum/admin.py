from django.contrib import admin

from .models import Thread, Post, Comment


admin.site.register(Thread)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'creator', 'created']
    search_fields = ['title', 'topic', 'creator', 'created']

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.fields = ['creator', 'created', 'topic', 'title', 'question']
            self.readonly_fields = ['creator', 'created']
        else:
            self.fields = ['topic', 'title', 'question']
            self.readonly_fields = []
        return super(PostAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.creator = user
        instance.save()
        return instance


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'creator', 'created']
    search_fields = ['post', 'creator', 'created']

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.fields = ['creator', 'created', 'post', 'reply']
            self.readonly_fields = ['post', 'creator', 'created']
        else:
            self.fields = ['post', 'reply']
            self.readonly_fields = []
        return super(CommentAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.creator = user
        instance.save()
        return instance
