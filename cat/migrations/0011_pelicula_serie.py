# Generated by Django 2.2.4 on 2019-08-30 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0010_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='serie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cat.Serie'),
            preserve_default=False,
        ),
    ]
