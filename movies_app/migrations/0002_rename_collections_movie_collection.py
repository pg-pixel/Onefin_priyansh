# Generated by Django 4.2.7 on 2023-11-23 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='collections',
            new_name='collection',
        ),
    ]
