# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 03:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isharonline', '0003_auto_20171028_0302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meditations',
            old_name='Publication',
            new_name='PublicationYear',
        ),
    ]