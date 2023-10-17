from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    fields = ['name', 'slug', 'parent', 'image']
    prepopulated_fields = {"slug": ("name",)}


admin.site.site_title = 'Админ-панель категорий'
admin.site.site_header = 'Админ-панель категорий'
