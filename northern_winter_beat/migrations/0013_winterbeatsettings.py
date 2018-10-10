# Generated by Django 2.1 on 2018-10-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('northern_winter_beat', '0012_auto_20181009_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinterbeatSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_text_da', models.TextField(default='', help_text='the paragraph above the list of bands. Is hidden if empty', verbose_name='Top text [danish]')),
                ('top_text_en', models.TextField(default='', help_text='the paragraph above the list of bands. Is hidden if empty', verbose_name='Top text [english]')),
                ('bottom_text_da', models.TextField(default='', help_text='The paragraph below the list of bands. It is hidden if empty', verbose_name='Bottom text [danish]')),
                ('bottom_text_en', models.TextField(default='', help_text='The paragraph below the list of bands. It is hidden if empty', verbose_name='Bottom text [english]')),
                ('description', models.TextField(default='', help_text='The description that is used when linking to winterbeat from another page', verbose_name='Description')),
                ('show_nav_bar', models.BooleanField(default=False, help_text='Show the bar of pages on top or not.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]