# Generated by Django 3.1.4 on 2020-12-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Title')),
                ('facebook_link', models.CharField(db_index=True, max_length=100, verbose_name='facebook')),
                ('insragram_link', models.CharField(db_index=True, max_length=100, verbose_name='instagram')),
                ('image', models.ImageField(blank=True, upload_to='media/follow_us', verbose_name='insagram_icon')),
                ('status', models.BooleanField(default=True, verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Follow_us',
                'verbose_name_plural': 'Follow_us',
                'db_table': 'follow_us',
            },
        ),
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'footer_info',
                'verbose_name_plural': 'footer_infos',
                'db_table': 'footer_info',
                'ordering': ('-created_at', 'title'),
            },
        ),
        migrations.CreateModel(
            name='FooterSubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_text', models.CharField(db_index=True, max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Footer_subscribe',
                'verbose_name_plural': 'Footer_subscribes',
                'db_table': 'footer_subscribe',
            },
        ),
        migrations.CreateModel(
            name='FooterSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Title')),
                ('status', models.BooleanField(default=True, verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Footer_support',
                'verbose_name_plural': 'Footer_supports',
                'db_table': 'footer_support',
                'ordering': ('-created_at', 'title'),
            },
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Menu Name')),
                ('status', models.BooleanField(default=True, verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sub_menu',
                'verbose_name_plural': 'Sub_menus',
                'db_table': 'sub_menu',
                'ordering': ('-created_at', 'title'),
            },
        ),
    ]
