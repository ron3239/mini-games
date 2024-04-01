# Generated by Django 5.0.2 on 2024-03-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_login', '0002_rename_user_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
