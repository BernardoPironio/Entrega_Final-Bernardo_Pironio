# Generated by Django 3.0.14 on 2022-12-16 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221216_1107'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PrePost',
            new_name='Post',
        ),
    ]
