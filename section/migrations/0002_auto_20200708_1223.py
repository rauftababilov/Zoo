# Generated by Django 3.0.8 on 2020-07-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creepingaccounting',
            name='growth',
            field=models.DecimalField(decimal_places=2, help_text='Измеряется в см.', max_digits=20, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='creepingaccounting',
            name='weight',
            field=models.DecimalField(decimal_places=3, help_text='Измеряется в кг.', max_digits=20, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='flyingaccounting',
            name='growth',
            field=models.DecimalField(decimal_places=2, help_text='Измеряется в см.', max_digits=20, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='flyingaccounting',
            name='weight',
            field=models.DecimalField(decimal_places=3, help_text='Измеряется в кг.', max_digits=20, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='shaggyaccounting',
            name='growth',
            field=models.DecimalField(decimal_places=2, help_text='Измеряется в см.', max_digits=20, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='shaggyaccounting',
            name='weight',
            field=models.DecimalField(decimal_places=3, help_text='Измеряется в кг.', max_digits=20, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='waterfowlaccounting',
            name='growth',
            field=models.DecimalField(decimal_places=2, help_text='Измеряется в см.', max_digits=20, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='waterfowlaccounting',
            name='weight',
            field=models.DecimalField(decimal_places=3, help_text='Измеряется в кг.', max_digits=20, verbose_name='Вес'),
        ),
    ]
