# Generated by Django 5.0.6 on 2024-06-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_alter_code_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='domain',
            field=models.CharField(),
        ),
    ]