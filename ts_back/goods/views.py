from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializers import *


class GoodsAPIListPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'


class GoodsViewSet(viewsets.ModelViewSet):
    """Viewset товаров выбранной категории"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    serializer_detail_class = GoodsDetailSerializer
    lookup_field = 'slug'
    pagination_class = GoodsAPIListPagination

    def get_queryset(self):
        if 'category' in self.request.GET:
            cat = self.request.GET['category']
            return Goods.objects.filter(category__slug=cat).select_related('category')

        return super().get_queryset()

    def get_serializer_class(self):
        """
        Если запрос по конкретному товару,
        используем сериалайзер с хар-ками
        """
        if self.kwargs.get('slug'):
            return self.serializer_detail_class

        return super().get_serializer_class()


