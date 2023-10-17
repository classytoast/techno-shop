# Generated by Django 4.2.6 on 2023-10-16 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('model', models.CharField(blank=True, max_length=250, null=True, verbose_name='модель')),
                ('description', models.TextField(max_length=3000, verbose_name='описание')),
                ('price', models.PositiveIntegerField(verbose_name='цена')),
                ('discounted_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(verbose_name='кол-во товара в наличии')),
                ('warranty', models.PositiveSmallIntegerField(verbose_name='гарантия в мес.')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cat_goods', to='catalog.category', verbose_name='категория')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='производитель')),
                ('country', models.CharField(blank=True, max_length=55, null=True, verbose_name='страна')),
                ('image', models.ImageField(blank=True, null=True, upload_to='manufacturers/%Y/%m/%d/', verbose_name='лого производителя')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img_of_post/%Y/%m/%d/', verbose_name='изображение')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.goods', verbose_name='товар')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsCharacteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=55, null=True, verbose_name='размер')),
                ('weight', models.CharField(blank=True, max_length=55, null=True, verbose_name='вес')),
                ('production_year', models.PositiveSmallIntegerField(blank=True, max_length=4, null=True, verbose_name='год производства')),
                ('material', models.CharField(blank=True, max_length=255, null=True, verbose_name='материал ')),
                ('color', models.CharField(blank=True, max_length=55, null=True, verbose_name='цвет')),
                ('display', models.TextField(blank=True, max_length=500, null=True, verbose_name='хар-ки экрана')),
                ('operating_system', models.TextField(blank=True, max_length=500, null=True, verbose_name='операционная система')),
                ('camera', models.TextField(blank=True, max_length=500, null=True, verbose_name='камера')),
                ('audio', models.TextField(blank=True, max_length=500, null=True, verbose_name='хар-ки звука')),
                ('battery', models.TextField(blank=True, max_length=500, null=True, verbose_name='хар-ки аккумулятора')),
                ('smart_tv', models.TextField(blank=True, max_length=500, null=True, verbose_name='хар-ки Smart TV')),
                ('processor', models.TextField(blank=True, max_length=500, null=True, verbose_name='процессор')),
                ('ram', models.TextField(blank=True, max_length=500, null=True, verbose_name='оперативная память')),
                ('video_card', models.TextField(blank=True, max_length=500, null=True, verbose_name='видеокарта')),
                ('data_storage', models.TextField(blank=True, max_length=500, null=True, verbose_name='накопители данных')),
                ('built_in_accessories', models.TextField(blank=True, max_length=1000, null=True, verbose_name='встроенное дополнительное оборудование')),
                ('peripheral_connectors', models.TextField(blank=True, max_length=1000, null=True, verbose_name='разъемы периферии')),
                ('additional_information', models.TextField(blank=True, max_length=1000, null=True, verbose_name='дополнительная информация')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='категория')),
                ('goods', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='товар')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='man_goods', to='goods.manufacturer', verbose_name='производитель')),
            ],
        ),
    ]
