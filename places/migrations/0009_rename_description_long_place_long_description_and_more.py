# Generated by Django 4.2 on 2024-02-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_image_number_pic_alter_place_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RemoveField(
            model_name='place',
            name='description_short',
        ),
        migrations.AddField(
            model_name='place',
            name='short_description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='media/', verbose_name='Картинка'),
        ),
    ]