# Generated by Django 2.1 on 2018-09-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('northern_winter_beat', '0005_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='concert',
            name='slug',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
