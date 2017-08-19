from django.contrib import admin
from django.utils import timezone

from .models import Newsletter, Subscriber


admin.site.register(Subscriber)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created', 'publish']
    search_fields = ['subject', 'created', 'publish']

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.fields = ['creator', 'subject', 'body', 'publish']
            if obj.publish < timezone.now():
                self.readonly_fields = ['creator', 'subject', 'body', 'publish']
            else:
                self.readonly_fields = ['creator']
        else:
            self.fields = ['subject', 'body', 'publish']
            self.readonly_fields = []
        return super(NewsletterAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.creator = user
        instance.save()
        return instance
