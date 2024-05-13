# Generated by Django 5.0.4 on 2024-05-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_appsdescriptions_active_summary_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsdescriptions',
            name='app_gh_url',
            field=models.URLField(default='https://https://github.com/ZichKoding'),
        ),
        migrations.AddField(
            model_name='appsdescriptions',
            name='app_url',
            field=models.URLField(default='https://zichkoding.com'),
        ),
    ]
