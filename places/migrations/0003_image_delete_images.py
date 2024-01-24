# Generated by Django 4.2 on 2024-01-24 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_pic', models.IntegerField(blank=True, null=True, verbose_name='Номер картинки')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.place', verbose_name='Место')),
            ],
            options={
                'ordering': ['number_pic'],
            },
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
