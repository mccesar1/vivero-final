# Generated by Django 4.0.6 on 2022-07-15 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNoticias', '0004_delete_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=20)),
                ('imagen', models.ImageField(upload_to='imgs/')),
            ],
            options={
                'verbose_name_plural': 'Imagenes',
            },
        ),
    ]
