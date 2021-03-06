# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-16 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bridegroom', '0010_auto_20160516_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneseen',
            name='bridegroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_no_views', to='bridegroom.BrideGroom'),
        ),
        migrations.AlterField(
            model_name='phoneseen',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='bridegroom.BrideGroom'),
        ),
    ]
