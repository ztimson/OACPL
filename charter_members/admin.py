from django.contrib import admin

from .models import Region, Position, Attorney


admin.site.register(Region)
admin.site.register(Position)


@admin.register(Attorney)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'position', 'region', 'phone_formatted', 'email', 'front_page', 'order', 'joined', 'thumbnail']
    list_filter = ['region', 'position', 'front_page', 'joined']
    search_fields = ['email', 'joined', 'last_name', 'first_name', 'region', 'position', 'website', 'phone', 'phone_formatted']
    fields = ['image_preview', 'image', 'last_name', 'first_name', 'position', 'region', 'biography', 'phone', 'email', 'website', 'front_page', 'order', 'joined']
    readonly_fields = ['image_preview']
