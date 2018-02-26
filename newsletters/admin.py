from django.contrib import admin

from .models import Attachment, Newsletter, Subscriber


admin.site.register(Attachment)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
    list_filter = ['date']
    search_fields = ['email']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created', 'publish']
    search_fields = ['subject', 'created', 'publish']
    filter_horizontal = ['attachments']

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.fields = ['creator', 'subject', 'body', 'sent', 'publish', 'attachments']
            if obj.sent:
                self.readonly_fields = ['creator', 'subject', 'body', 'sent', 'publish', 'attachments']
            else:
                self.readonly_fields = ['creator', 'sent']
        else:
            self.fields = ['subject', 'body', 'publish', 'attachments']
            self.readonly_fields = []
        return super(NewsletterAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.creator = user
        instance.save()
        return instance
