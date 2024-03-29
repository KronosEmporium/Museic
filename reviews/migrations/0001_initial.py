# Generated by Django 2.2 on 2019-06-13 01:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewtitle', models.CharField(max_length=255)),
                ('reviewdatetime', models.DateTimeField(auto_now_add=True)),
                ('reviewtext', models.TextField(blank=True, null=True)),
                ('reviewupvotes', models.IntegerField(default=0)),
                ('reviewdownvotes', models.IntegerField(default=0)),
                ('uservote', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'reviews',
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewsvotedon', models.ManyToManyField(blank=True, to='reviews.Review')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songtitle', models.CharField(max_length=255)),
                ('songlink', models.URLField(blank=True)),
                ('songartist', models.CharField(max_length=255)),
                ('songrating', models.IntegerField(default=0)),
                ('ratingcount', models.IntegerField(default=0)),
                ('songreviews', models.ManyToManyField(blank=True, to='reviews.Review')),
            ],
            options={
                'verbose_name_plural': 'songs',
                'db_table': 'song',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='reviewsong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reviews.Song'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
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
