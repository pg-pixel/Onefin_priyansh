# Generated by Django 4.2.7 on 2023-11-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0008_movie_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='uuid',
            field=models.UUIDField(),
        ),
    ]
