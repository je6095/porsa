# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address_1',
            field=models.CharField(default='', max_length=100, verbose_name='Address 1'),
        ),
        migrations.AddField(
            model_name='event',
            name='address_2',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Address 2'),
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default='', max_length=25, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='event',
            name='end_onlydate',
            field=models.DateField(default=None, verbose_name='end date'),
        ),
        migrations.AddField(
            model_name='event',
            name='end_onlytime',
            field=models.TimeField(default=None, verbose_name='end time'),
        ),
        migrations.AddField(
            model_name='event',
            name='pallet',
            field=models.IntegerField(default=0, verbose_name='Pallet Count'),
        ),
        migrations.AddField(
            model_name='event',
            name='phone',
            field=models.CharField(default='', max_length=12, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='event',
            name='pick',
            field=models.CharField(default='', max_length=6, verbose_name='Pick List'),
        ),
        migrations.AddField(
            model_name='event',
            name='sales_order',
            field=models.CharField(default='', max_length=8, verbose_name='Sales Order'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_onlydate',
            field=models.DateField(default=None, verbose_name='start date'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_onlytime',
            field=models.TimeField(default=None, verbose_name='start time'),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(default='', max_length=25, verbose_name='State/Province'),
        ),
        migrations.AddField(
            model_name='event',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Total Weight'),
        ),
        migrations.AddField(
            model_name='event',
            name='zipcode',
            field=models.CharField(default='', max_length=10, verbose_name='ZIP/Postal Code'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(blank=True, default='', verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(blank=True, default='', verbose_name='start date'),
        ),
    ]
