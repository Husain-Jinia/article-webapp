# Generated by Django 4.0.4 on 2022-04-13 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_articles_posted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
