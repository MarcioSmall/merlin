from django.contrib import admin

from .models import Variable


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = ('name_var', 'value_var', 'description', 'author')


