# Generated by Django 3.0.14 on 2022-12-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prepost',
            name='autor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='prepost',
            name='subtitulo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='prepost',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
