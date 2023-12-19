# Generated by Django 5.0 on 2023-12-19 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of genre')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Singer name')),
                ('bio', models.TextField(verbose_name='biography')),
                ('photo', models.ImageField(default='default.png', upload_to='albums/', verbose_name='Image')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Singer',
                'verbose_name_plural': 'Singers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('duration', models.CharField(max_length=4, verbose_name='Duration of track')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text of track')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year of production')),
                ('num_of_tracks', models.IntegerField(verbose_name='Number of tracks')),
                ('duration', models.CharField(max_length=5, verbose_name='Duration of album')),
                ('cover', models.ImageField(default='cover.png', upload_to='albums/', verbose_name='Cover')),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_genre', to='catalog.genre')),
                ('singer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='album_singer', to='catalog.singer')),
                ('track', models.ManyToManyField(related_name='album_track', to='catalog.track')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
                'ordering': ['year'],
                'indexes': [models.Index(fields=['created_at'], name='catalog_alb_created_fa0bb7_idx')],
            },
        ),
    ]
