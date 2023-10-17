from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    """Viewset главной страницы"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'cats': cats.name})
