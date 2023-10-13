from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование категории')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    parent = models.ForeignKey('self', related_name="children",
                               on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="categories/%Y/%m/%d/", blank=True,
                              verbose_name='фото категории', null=True)
