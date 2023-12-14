# Generated by Django 5.0 on 2023-12-13 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_remove_album_track_album_track'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('nickname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nickname')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='Biography')),
                ('avatar', models.ImageField(default='default.png', upload_to='users/', verbose_name='Avatar')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('favourites', models.ManyToManyField(blank=True, default=None, related_name='favourite_album', to='catalog.album')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]