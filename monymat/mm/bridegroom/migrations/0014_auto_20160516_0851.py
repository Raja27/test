# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-16 08:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bridegroom', '0013_auto_20160516_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='family', to=settings.AUTH_USER_MODEL),
        ),
    ]