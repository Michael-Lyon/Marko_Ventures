from django.contrib import admin
from .models import Item

admin.site.site_header = 'Marko Admin Dashboard'
admin.site.register(Item)
