# Generated by Django 2.0.1 on 2018-06-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LongToShortURL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='longtoshort',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
