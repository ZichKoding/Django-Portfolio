# Generated by Django 5.0.4 on 2024-05-19 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_categories_remove_appsdescriptions_app_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
