from collections import OrderedDict

from rest_framework import serializers

from .models import *


class GoodsSerializer(serializers.ModelSerializer):
    """Сериалайзер товаров в выбранной категории"""
    class Meta:
        model = Goods
        fields = ('name', 'slug', 'category',
                  'model', 'price',
                  'discounted_price', 'quantity')
        lookup_field = 'slug'


class GoodsCharacteristicsSerializer(serializers.ModelSerializer):
    """товар со всеми характеристиками"""

    class Meta:
        model = GoodsCharacteristics
        fields = '__all__'

    def to_representation(self, instance):
        result = super(GoodsCharacteristicsSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key]])


class GoodsDetailSerializer(serializers.ModelSerializer):
    """товар со всеми характеристиками"""
    chars = GoodsCharacteristicsSerializer()

    class Meta:
        model = Goods
        fields = '__all__'
        lookup_field = 'slug'

