from django.contrib import admin

from .models import Position, Attorney


admin.site.register(Position)


@admin.register(Attorney)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone_formatted', 'email', 'front_page', 'joined', 'thumbnail')
    list_filter = ['position', 'front_page', 'joined']
    search_fields = ('bio', 'email', 'joined', 'name', 'position', 'website', 'phone', 'phone_formatted')
    fields = ('image_preview', 'image', 'name', 'position', 'bio', 'phone', 'email', 'website', 'front_page', 'joined')
    readonly_fields = ('image_preview',)
