# Generated by Django 3.1.6 on 2021-03-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opgas', '0004_auto_20210308_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='photo',
            field=models.ImageField(null=True, upload_to='p_images'),
        ),
    ]
