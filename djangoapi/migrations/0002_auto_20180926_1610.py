# Generated by Django 2.1.1 on 2018-09-26 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientemodel',
            old_name='tipoCliente',
            new_name='tipo_cliente',
        ),
        migrations.RenameField(
            model_name='espaciomodel',
            old_name='tipoCarro',
            new_name='tipo_carro',
        ),
        migrations.RenameField(
            model_name='parqueaderomodel',
            old_name='numEspacios',
            new_name='num_espacios',
        ),
    ]