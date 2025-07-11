# Generated by Django 5.2 on 2025-05-07 19:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0002_franchise_img_alter_franchise_city_and_more'),
        ('posts', '0003_alter_post_categories_alter_post_img_alter_post_link'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Title',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, to='posts.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='post',
            name='franchise',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='franchise.franchise', verbose_name='Franchise'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='posts', verbose_name='Img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Updated'),
        ),
    ]
