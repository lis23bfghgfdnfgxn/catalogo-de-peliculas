# Generated by Django 2.2.4 on 2019-08-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0007_pelicula_url_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='sinopsis',
            field=models.TextField(max_length=500),
        ),
    ]
