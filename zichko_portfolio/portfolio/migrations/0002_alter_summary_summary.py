# Generated by Django 5.0.4 on 2024-05-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='summary',
            field=models.CharField(max_length=300),
        ),
    ]
