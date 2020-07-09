# Generated by Django 3.0.7 on 2020-07-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0004_auto_20200708_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creepinganimal',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название животного'),
        ),
        migrations.AlterField(
            model_name='flyinganimal',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название животного'),
        ),
        migrations.AlterField(
            model_name='shaggyanimal',
            name='count_teeth',
            field=models.IntegerField(verbose_name='Количество зубов'),
        ),
        migrations.AlterField(
            model_name='shaggyanimal',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название животного'),
        ),
        migrations.AlterField(
            model_name='waterfowlanimal',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название животного'),
        ),
    ]