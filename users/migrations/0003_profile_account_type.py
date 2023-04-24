# Generated by Django 3.2.18 on 2023-04-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('full', 'Полный пакет'), ('free', 'Бесплатный пакет')], default='free', max_length=30),
        ),
    ]