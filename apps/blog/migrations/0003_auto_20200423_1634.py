# Generated by Django 3.0.5 on 2020-04-23 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='catetoria',
            new_name='categoria',
        ),
    ]
