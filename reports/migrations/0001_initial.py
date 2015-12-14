# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crime_type', models.CharField(max_length=255)),
                ('crime_type_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=255)),
                ('location_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_date', models.DateField()),
                ('loss', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('crime_type', models.ForeignKey(to='reports.CrimeType')),
                ('location', models.ForeignKey(to='reports.Location')),
            ],
        ),
    ]
