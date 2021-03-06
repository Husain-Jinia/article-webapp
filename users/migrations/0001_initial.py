# Generated by Django 4.0.4 on 2022-04-15 15:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpeg', upload_to='profile_pics')),
                ('phone_number', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('dob', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('category', models.ManyToManyField(related_name='profile', to='article.category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
