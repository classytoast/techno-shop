# Generated by Django 4.2.6 on 2023-10-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_goods_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='additional_information',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='audio',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='хар-ки звука'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='battery',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='хар-ки аккумулятора'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='built_in_accessories',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='встроенное дополнительное оборудование'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='camera',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='камера'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=55, null=True, verbose_name='цвет'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='data_storage',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='накопители данных'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='display',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='хар-ки экрана'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='material',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='материал '),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='operating_system',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='операционная система'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='peripheral_connectors',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='разъемы периферии'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='processor',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='процессор'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='production_year',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='год производства'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='ram',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='оперативная память'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='size',
            field=models.CharField(blank=True, default=None, max_length=55, null=True, verbose_name='размер'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='smart_tv',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='хар-ки Smart TV'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='video_card',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='видеокарта'),
        ),
        migrations.AlterField(
            model_name='goodscharacteristics',
            name='weight',
            field=models.CharField(blank=True, default=None, max_length=55, null=True, verbose_name='вес'),
        ),
    ]