# Generated by Django 4.0.4 on 2022-04-14 22:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0009_alter_articles_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislike_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]