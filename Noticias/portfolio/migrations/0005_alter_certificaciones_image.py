# Generated by Django 4.0.6 on 2023-01-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_certificaciones_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificaciones',
            name='image',
            field=models.ImageField(upload_to='imgs/'),
        ),
    ]
