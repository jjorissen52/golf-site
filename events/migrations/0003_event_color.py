# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-04 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20171103_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='color',
            field=models.CharField(choices=[('#FFFFFF', 'White'), ('#C0C0C0', 'Silver'), ('#808080', 'Gray'), ('#000000', 'Black'), ('#FF0000', 'Red'), ('#800000', 'Maroon'), ('#FFFF00', 'Yellow'), ('#808000', 'Olive'), ('#00FF00', 'Lime'), ('#008000', 'Green'), ('#00FFFF', 'Aqua'), ('#008080', 'Teal'), ('#0000FF', 'Blue'), ('#000080', 'Navy'), ('#FF00FF', 'Fuchsia'), ('#800080', 'Purple')], default='#0000FF', max_length=7),
        ),
    ]