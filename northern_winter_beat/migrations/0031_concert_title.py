# Generated by Django 2.1.4 on 2018-12-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('northern_winter_beat', '0030_auto_20181210_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='title',
            field=models.CharField(blank=True, help_text='If you want the title to be something else than the artist name', max_length=128, null=True, verbose_name='title'),
        ),
    ]
