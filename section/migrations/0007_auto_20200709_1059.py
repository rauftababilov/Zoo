# Generated by Django 3.0.8 on 2020-07-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0006_auto_20200709_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='creepingaccounting',
            name='animal_name',
            field=models.CharField(max_length=40, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='flyingaccounting',
            name='animal_name',
            field=models.CharField(max_length=40, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='shaggyaccounting',
            name='animal_name',
            field=models.CharField(max_length=40, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='waterfowlaccounting',
            name='animal_name',
            field=models.CharField(max_length=40, null=True, verbose_name='Имя'),
        ),
    ]