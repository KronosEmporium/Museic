# Generated by Django 2.2.2 on 2019-06-06 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20190606_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewsong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reviews.Song'),
        ),
    ]
