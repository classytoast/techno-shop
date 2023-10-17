from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер категорий товаров на сайте"""
    class Meta:
        model = Category
        fields = "__all__"
        lookup_field = 'slug'

