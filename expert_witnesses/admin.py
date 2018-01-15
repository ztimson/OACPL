from django.contrib import admin

from .models import Expert, AreaOfExpertise


admin.site.register(AreaOfExpertise)


@admin.register(Expert)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['name', 'institute', 'CV']
    list_filter = ['institute', 'expertise']
    search_fields = ['name', 'institute', 'expertise']
    fields = ['name', 'institute', 'CV', 'expertise', 'cases']
    filter_horizontal = ['expertise', 'cases']
