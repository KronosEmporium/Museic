# Generated by Django 2.2.2 on 2019-06-06 20:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20190606_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='songreviews',
            field=models.ManyToManyField(blank=True, to='reviews.Review'),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistname', models.CharField(max_length=255)),
                ('artistgenre', models.CharField(max_length=255)),
                ('artistrating', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('artistsongs', models.ManyToManyField(blank=True, to='reviews.Song')),
            ],
            options={
                'verbose_name_plural': 'artists',
                'db_table': 'artist',
            },
        ),
    ]