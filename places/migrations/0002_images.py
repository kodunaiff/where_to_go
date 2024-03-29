# Generated by Django 4.2 on 2024-01-24 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.place')),
            ],
        ),
    ]
