# Generated by Django 4.2 on 2024-02-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_image_number_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Короткое описание'),
        ),
    ]
