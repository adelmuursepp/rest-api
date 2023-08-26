# Generated by Django 3.2.15 on 2022-12-20 01:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price_range', models.FloatField(blank=True, null=True)),
                ('parent_company', models.CharField(blank=True, max_length=40, null=True)),
                ('urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None)),
                ('goy_link', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('planet_goy_rating', models.FloatField(blank=True, null=True)),
                ('people_goy_rating', models.FloatField(blank=True, null=True)),
                ('animal_goy_rating', models.FloatField(blank=True, null=True)),
                ('policy_fti_rating', models.FloatField(blank=True, null=True)),
                ('governance_fti_rating', models.FloatField(blank=True, null=True)),
                ('knowshow_fti_rating', models.FloatField(blank=True, null=True)),
                ('spotlight_fti_rating', models.FloatField(blank=True, null=True)),
                ('traceability_fti_rating', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]