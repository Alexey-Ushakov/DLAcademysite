# Generated by Django 3.2.8 on 2021-10-10 13:52

import advito.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=500, verbose_name='о себе')),
                ('avatar', models.ImageField(upload_to=advito.models.user_avatar_path, verbose_name='фото пользователя')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='день рождения')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
