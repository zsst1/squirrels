# Generated by Django 2.2.7 on 2019-12-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField(verbose_name='Latitude')),
                ('longitude', models.IntegerField(verbose_name='Longitude')),
                ('unique_squirrel_id', models.CharField(max_length=200, verbose_name='Unique Squirrel ID')),
                ('shift', models.CharField(max_length=200, verbose_name='Shift')),
                ('date', models.IntegerField(verbose_name='Date')),
                ('age', models.CharField(max_length=200, verbose_name='Age')),
                ('primary_fur_color', models.CharField(max_length=200, verbose_name='Primary Fur Color')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('specific_location', models.CharField(max_length=200, verbose_name='Specific Location')),
                ('running', models.BooleanField(verbose_name='Running')),
                ('chasing', models.BooleanField(verbose_name='Chasing')),
                ('climbing', models.BooleanField(verbose_name='Climbing')),
                ('eating', models.BooleanField(verbose_name='Eating')),
                ('other_activities', models.CharField(max_length=200, verbose_name='Other Activities')),
                ('kuks', models.BooleanField(verbose_name='Kuks')),
                ('quaas', models.BooleanField(verbose_name='Quaas')),
                ('moans', models.BooleanField(verbose_name='Moans')),
                ('tail_flags', models.BooleanField(verbose_name='Tail flags')),
                ('tail_twitches', models.BooleanField(verbose_name='Tail twithces')),
                ('approaches', models.BooleanField(verbose_name='Approaches')),
                ('indifferent', models.BooleanField(verbose_name='Indifferent')),
                ('runs_from', models.BooleanField(verbose_name='Runs from')),
            ],
        ),
    ]