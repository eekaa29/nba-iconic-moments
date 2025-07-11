# Generated by Django 5.2 on 2025-05-07 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0002_franchise_img_alter_franchise_city_and_more'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='franchise',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='franchise.franchise', verbose_name='Autor'),
        ),
    ]
