from django.contrib import admin
from django.urls import path, include

from catalog.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', CategoryViewSet, basename='categories')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
