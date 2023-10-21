from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер категорий товаров на сайте"""
    class Meta:
        model = Category
        fields = ('name', 'slug', 'parent', 'image')
        lookup_field = 'slug'

