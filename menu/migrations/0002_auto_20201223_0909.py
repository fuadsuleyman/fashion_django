# Generated by Django 3.1.4 on 2020-12-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followus',
            name='image',
            field=models.ImageField(blank=True, upload_to='follow_us', verbose_name='insagram_icon'),
        ),
    ]