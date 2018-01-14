from django.contrib import admin

from .models import Chapter, Position, Attorney


admin.site.register(Chapter)
admin.site.register(Position)


@admin.register(Attorney)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'chapter', 'phone_formatted', 'email', 'front_page', 'joined', 'thumbnail')
    list_filter = ['chapter', 'position', 'front_page', 'joined']
    search_fields = ('email', 'joined', 'name', 'chapter', 'position', 'website', 'phone', 'phone_formatted')
    fields = ('image_preview', 'image', 'name', 'position', 'chapter', 'biography', 'phone', 'email', 'website', 'front_page', 'joined')
    readonly_fields = ('image_preview',)
