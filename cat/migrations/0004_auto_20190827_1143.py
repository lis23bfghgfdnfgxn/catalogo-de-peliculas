# Generated by Django 2.2.4 on 2019-08-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0003_auto_20190827_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='fecha_estreno',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='sinopsis',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
