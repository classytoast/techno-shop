from django.db import models

from catalog.models import Category


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name='производитель')
    country = models.CharField(max_length=55, null=True, blank=True, verbose_name='страна')
    image = models.ImageField(upload_to="manufacturers/%Y/%m/%d/", blank=True,
                              verbose_name='лого производителя', null=True)


class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name="cat_goods", verbose_name='категория')
    model = models.CharField(max_length=250, null=True, blank=True, verbose_name='модель')
    description = models.TextField(max_length=3000, verbose_name='описание')
    price = models.PositiveIntegerField(verbose_name='цена')
    discounted_price = models.PositiveIntegerField(null=True, blank=True, verbose_name='цена')
    quantity = models.PositiveIntegerField(verbose_name='кол-во товара в наличии')
    warranty = models.PositiveSmallIntegerField(verbose_name='гарантия в мес.')


class GoodsCharacteristics(models.Model):
    goods = models.OneToOneField(Goods, on_delete=models.CASCADE,
                                 verbose_name='товар')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 verbose_name='категория')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE,
                                     related_name="man_goods", verbose_name='производитель')
    size = models.CharField(max_length=55, null=True, blank=True,
                            verbose_name='размер')
    weight = models.CharField(max_length=55, null=True, blank=True,
                              verbose_name="вес")
    production_year = models.PositiveSmallIntegerField(max_length=4, null=True, blank=True,
                                                       verbose_name='год производства')
    material = models.CharField(max_length=255, null=True, blank=True,
                                verbose_name='материал ')
    color = models.CharField(max_length=55, null=True, blank=True,
                             verbose_name='цвет')
    display = models.TextField(max_length=500, null=True, blank=True,
                               verbose_name='хар-ки экрана')
    operating_system = models.TextField(max_length=500, null=True, blank=True,
                                        verbose_name='операционная система')
    camera = models.TextField(max_length=500, null=True, blank=True,
                              verbose_name='камера')
    audio = models.TextField(max_length=500, null=True, blank=True,
                             verbose_name='хар-ки звука')
    battery = models.TextField(max_length=500, null=True, blank=True,
                               verbose_name='хар-ки аккумулятора')
    smart_tv = models.TextField(max_length=500, null=True, blank=True,
                                verbose_name='хар-ки Smart TV')
    processor = models.TextField(max_length=500, null=True, blank=True,
                                 verbose_name='процессор')
    ram = models.TextField(max_length=500, null=True, blank=True,
                           verbose_name='оперативная память')
    video_card = models.TextField(max_length=500, null=True, blank=True,
                                  verbose_name='видеокарта')
    data_storage = models.TextField(max_length=500, null=True, blank=True,
                                    verbose_name='накопители данных')
    built_in_accessories = models.TextField(max_length=1000, null=True, blank=True,
                                            verbose_name='встроенное дополнительное оборудование')
    peripheral_connectors = models.TextField(max_length=1000, null=True, blank=True,
                                             verbose_name='разъемы периферии')
    additional_information = models.TextField(max_length=1000, null=True, blank=True,
                                              verbose_name='дополнительная информация')


class GoodsImage(models.Model):
    img = models.ImageField(upload_to="img_of_post/%Y/%m/%d/", verbose_name='изображение')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='images', verbose_name='товар')