from django.contrib import admin

from .models import Expert, AreaOfExpertise


admin.site.register(AreaOfExpertise)


@admin.register(Expert)
class ExpertiseAdmin(admin.ModelAdmin):
    fields = ['name', 'institute', 'expertise', 'cases']
    filter_horizontal = ('expertise', 'cases')
