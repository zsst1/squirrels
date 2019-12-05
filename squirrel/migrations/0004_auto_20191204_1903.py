# Generated by Django 2.2.7 on 2019-12-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0003_auto_20191204_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Longitude'),
        ),
    ]