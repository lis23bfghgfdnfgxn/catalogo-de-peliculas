# Generated by Django 2.2.4 on 2019-08-26 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edo', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('sinopsis', models.CharField(max_length=250, unique=True)),
                ('director', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_estreno', models.DateField(blank=True, null=True)),
                ('duracion', models.CharField(max_length=15, unique=True)),
                ('imagen', models.URLField(max_length=1000)),
                ('genero', models.ManyToManyField(blank=True, to='cat.Genero')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Peliculas',
            },
        ),
    ]
