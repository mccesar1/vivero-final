# Generated by Django 4.0.2 on 2022-06-13 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNoticias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('servicio_imagen', models.ImageField(upload_to='imgs/')),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
