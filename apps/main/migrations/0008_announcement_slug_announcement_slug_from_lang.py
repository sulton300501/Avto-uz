# Generated by Django 5.1.6 on 2025-02-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_bodystatus_body_part_alter_bodystatus_car_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='slug_from_lang',
            field=models.CharField(blank=True, choices=[('uz', "o'zbekcha"), ('ru', 'ruscha')], max_length=64, null=True, verbose_name='slug tilini tanlang'),
        ),
    ]
