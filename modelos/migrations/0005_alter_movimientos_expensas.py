# Generated by Django 4.1.2 on 2022-10-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0004_movimientos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientos',
            name='expensas',
            field=models.CharField(choices=[('S', 'Corresponde'), ('N', 'No Corresponde')], max_length=1),
        ),
    ]
