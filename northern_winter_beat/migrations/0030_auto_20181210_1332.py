# Generated by Django 2.1.4 on 2018-12-10 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('northern_winter_beat', '0029_concert_sort_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concert',
            options={'verbose_name': 'concert', 'verbose_name_plural': 'concerts'},
        ),
        migrations.AlterField(
            model_name='concert',
            name='artist',
            field=models.ForeignKey(help_text='The artist that is going to play the concert', on_delete=django.db.models.deletion.CASCADE, to='northern_winter_beat.Artist', verbose_name='artist'),
        ),
    ]
