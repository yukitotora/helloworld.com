# Generated by Django 3.0.5 on 2020-05-29 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coment',
            new_name='Comment',
        ),
    ]
