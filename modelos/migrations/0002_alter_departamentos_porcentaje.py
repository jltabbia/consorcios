# Generated by Django 4.1.2 on 2022-10-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentos',
            name='porcentaje',
            field=models.FloatField(verbose_name='Porcentaje expensas'),
        ),
    ]
