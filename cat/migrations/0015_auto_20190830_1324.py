# Generated by Django 2.2.4 on 2019-08-30 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0014_auto_20190830_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat.Serie'),
        ),
    ]
