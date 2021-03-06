# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-16 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bridegroom', '0006_auto_20160516_0724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educations',
            old_name='higher_degree',
            new_name='name',
        ),
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
