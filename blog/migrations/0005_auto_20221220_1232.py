# Generated by Django 3.0.14 on 2022-12-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20221220_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
