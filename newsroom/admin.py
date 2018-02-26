from django.contrib import admin

from .models import Attachment, PressRelease


admin.site.register(Attachment)


@admin.register(PressRelease)
class PressRelease(admin.ModelAdmin):
    list_display = ['title', 'created', 'creator']
    fields = ['title', 'attachments']
    filter_horizontal = ['attachments']

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.creator = user
        instance.save()
        return instance
