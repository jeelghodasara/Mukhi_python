# Generated by Django 3.1.6 on 2021-02-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='p_images')),
                ('p_price', models.IntegerField()),
                ('p_bhk', models.IntegerField()),
                ('P_floor', models.IntegerField()),
                ('p_city', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
