# Generated by Django 5.0.6 on 2024-06-01 10:46

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1200)),
                ('price', models.IntegerField()),
                ('image_one', models.ImageField(upload_to='')),
                ('image_two', models.ImageField(upload_to='')),
                ('image_three', models.ImageField(upload_to='')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_create'],
            },
        ),
    ]
