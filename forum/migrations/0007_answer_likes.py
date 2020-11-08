# Generated by Django 3.1 on 2020-11-08 19:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0006_auto_20201108_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='answerLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
