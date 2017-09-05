from django.contrib import admin

from case_law.models import Decision, Subtitle

admin.site.register(Subtitle)


@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    fields = ['synopsis', 'headers', 'date', 'pdf']
    filter_horizontal = ['headers']
    list_display = ['synopsis', 'date']
