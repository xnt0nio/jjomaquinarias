# Generated by Django 5.0.6 on 2024-07-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_producto_equipamiento_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]