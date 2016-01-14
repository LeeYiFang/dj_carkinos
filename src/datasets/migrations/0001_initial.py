# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CellLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('primary_site', models.CharField(max_length=1024)),
                ('primary_histology', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('name', models.CharField(max_length=1024, primary_key=True, serialize=False)),
                ('data_path', models.FilePathField(blank=True, max_length=512, path='/Users/liang/code/dj_carkinos/data')),
            ],
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrez_id', models.IntegerField(blank=True, null=True)),
                ('gene_symbol', models.CharField(blank=True, max_length=256)),
                ('gene_name', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralPlatform',
            fields=[
                ('name', models.CharField(max_length=1024, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProbeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=256)),
                ('platform_order', models.IntegerField()),
                ('genes', models.ManyToManyField(related_name='probes', to='datasets.Gene')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('dataset_order', models.IntegerField()),
                ('cell_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='datasets.CellLine')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='datasets.DataSet')),
            ],
        ),
        migrations.CreateModel(
            name='MicroarrayPlatform',
            fields=[
                ('generalplatform_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasets.GeneralPlatform')),
                ('manufacturer', models.CharField(max_length=256)),
            ],
            bases=('datasets.generalplatform',),
        ),
        migrations.AddField(
            model_name='sample',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.GeneralPlatform'),
        ),
        migrations.AlterUniqueTogether(
            name='cellline',
            unique_together=set([('name', 'primary_site', 'primary_histology')]),
        ),
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together=set([('dataset', 'name'), ('dataset', 'dataset_order')]),
        ),
        migrations.AddField(
            model_name='probeinfo',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='probes', to='datasets.MicroarrayPlatform'),
        ),
        migrations.AlterUniqueTogether(
            name='probeinfo',
            unique_together=set([('platform', 'platform_order'), ('platform', 'identifier')]),
        ),
    ]
