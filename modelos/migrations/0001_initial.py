# Generated by Django 4.1.2 on 2022-10-06 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Propietarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=45, verbose_name='Apellido')),
                ('domicilio', models.CharField(blank=True, max_length=45, null=True, verbose_name='Domicilio')),
                ('contacto', models.CharField(blank=True, max_length=15, null=True, verbose_name='Tel. de Contacto')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electrónico')),
                ('cuit_cuil', models.CharField(max_length=15, verbose_name='CUIT/CUIL')),
            ],
            options={
                'verbose_name': 'Propietario',
                'verbose_name_plural': 'Propietarios',
                'db_table': 'propietarios',
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Edificios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre Edificio')),
                ('domicilio', models.CharField(max_length=45, verbose_name='Domicilio')),
                ('cantidad_dptos', models.IntegerField(default=0)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Administrador')),
            ],
            options={
                'verbose_name': 'Edificio',
                'verbose_name_plural': 'Edificios',
                'db_table': 'edificios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piso', models.IntegerField(verbose_name='Nro. de Piso')),
                ('numero', models.CharField(max_length=2, verbose_name='Nro. Departamento')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Porcentaje expensas')),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.edificios', verbose_name='Edificio')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.propietarios', verbose_name='Propietario')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'departamentos',
                'ordering': ['id'],
            },
        ),
    ]