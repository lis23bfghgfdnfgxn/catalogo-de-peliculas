# Generated by Django 2.2.4 on 2019-08-30 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0017_pelicula_serie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='serie',
        ),
    ]
