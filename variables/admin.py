from django.contrib import admin

from .models import Variable


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    fields = ['key', 'help_text', 'value']
    list_display = ['key', 'value', 'help_text']

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.readonly_fields = ['help_text', 'key']
        else:
            self.readonly_fields = []
        return super().get_form(request, obj, **kwargs)
