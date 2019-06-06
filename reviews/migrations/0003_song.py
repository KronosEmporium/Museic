# Generated by Django 2.2.2 on 2019-06-06 19:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20190606_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songtitle', models.CharField(max_length=255)),
                ('songlink', models.URLField()),
                ('songrating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('songreviews', models.ManyToManyField(to='reviews.Review')),
            ],
            options={
                'verbose_name_plural': 'songs',
                'db_table': 'song',
            },
        ),
    ]