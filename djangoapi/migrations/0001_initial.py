# Generated by Django 2.1.1 on 2018-09-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(blank=True, max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=150, unique=True)),
                ('edad', models.IntegerField()),
                ('nit', models.CharField(blank=True, max_length=100, unique=True)),
                ('tipoCliente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EspacioModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipoCarro', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OferenteModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=150, unique=True)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ParqueaderoModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('numEspacios', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReservaModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
