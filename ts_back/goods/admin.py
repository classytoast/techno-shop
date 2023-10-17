from django.contrib import admin

from .models import *


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    fields = ['name', 'country', 'image']


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'model',
                    'price', 'discounted_price', 'quantity']
    fields = ['name', 'slug', 'category', 'model',
              'description', 'price', 'discounted_price',
              'quantity', 'warranty']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(GoodsCharacteristics)
class GoodsCharacteristicsAdmin(admin.ModelAdmin):
    list_display = ['goods', 'category', 'production_year']
    fields = ['goods', 'category', 'manufacturer',
              'size', 'weight', 'production_year',
              'material', 'color', 'display', 'operating_system',
              'camera', 'audio', 'battery', 'smart_tv',
              'processor', 'ram', 'video_card', 'data_storage',
              'built_in_accessories', 'peripheral_connectors', 'additional_information']


@admin.register(GoodsImage)
class GoodsImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'goods']
    fields = ['img', 'goods']


admin.site.site_title = 'Админ-панель товаров'
admin.site.site_header = 'Админ-панель товаров'
