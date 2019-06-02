# Generated by Django 2.2.1 on 2019-06-02 23:26

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20190602_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название коллекции')),
                ('name_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='collection_img/', verbose_name='Изображение коллекции')),
                ('page_title', models.CharField(max_length=255, null=True, verbose_name='Название страницы')),
                ('page_description', models.TextField(null=True, verbose_name='Описание страницы')),
                ('page_keywords', models.TextField(null=True, verbose_name='Keywords')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание коллекции')),
                ('views', models.IntegerField(default=0)),
                ('show_at_homepage', models.BooleanField(default=True, verbose_name='Отображать на главной')),
                ('show_at_category', models.BooleanField(default=True, verbose_name='Отображать в категории')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.Filter', verbose_name='Фильтр'),
        ),
        migrations.AddField(
            model_name='item',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.Collection', verbose_name='В коллекции'),
        ),
    ]