# Generated by Django 3.1.4 on 2020-12-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_category_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='is_third'),
        ),
    ]