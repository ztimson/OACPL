from django.contrib import admin

from case_law.models import Case, Heading

admin.site.register(Heading)


@admin.register(Case)
class DecisionAdmin(admin.ModelAdmin):
    fields = ['synopsis', 'headings', 'published', 'pdf']
    filter_horizontal = ['headings']
    list_display = ['synopsis', 'published']
