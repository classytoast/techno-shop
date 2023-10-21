from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from catalog.views import *
from goods.views import *


router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'goods', GoodsViewSet, basename='goods')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
