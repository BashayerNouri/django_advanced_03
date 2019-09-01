from django.contrib import admin
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    # ...
    list_display = ('id', 'name','description')
    list_display_links = ('name','description')
    list_filter = ['name','description']
    search_fields = ['name']


admin.site.register(Store,StoreAdmin)

