# Generated by Django 3.1.7 on 2021-05-25 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('categoria_imagen', models.ImageField(upload_to='imgs/')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('detalles', models.TextField(max_length=20000)),
                ('imagen', models.ImageField(upload_to='imgs/')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppNoticias.categoria')),
            ],
            options={
                'verbose_name_plural': 'Noticias',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('comentario', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppNoticias.noticia')),
            ],
            options={
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
