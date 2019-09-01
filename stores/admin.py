from django.contrib import admin
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name','description','id')
    list_editable = ('description',)
    list_filter = ['name','description']
    search_fields = ['name']


admin.site.register(Store,StoreAdmin)

