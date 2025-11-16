from django.contrib import admin
from .models import Menu, MenuItem

admin.site.register(Menu)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'menu', 'parent', 'order']
    list_filter = ['menu', 'parent']
    search_fields = ['name']
    fields = ['menu', 'parent', 'name', 'url', 'named_url', 'order']

admin.site.register(MenuItem, MenuItemAdmin)
