from django.contrib import admin
from django.contrib.auth.admin import User
from django.utils import timezone

from .models import Newsletter, NewsletterSubscription


class SubscriberInline(admin.StackedInline):
    can_delete = False
    extra = 1
    fields = ['subscribed']
    max_num = 1
    model = NewsletterSubscription


class ExtendUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'newsletter', 'is_staff', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['is_staff', 'is_superuser']
    inlines = [SubscriberInline]

    def newsletter(self, obj):
        return bool(True)
    newsletter.boolean = True


admin.site.unregister(User)
admin.site.register(User, ExtendUserAdmin)


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
