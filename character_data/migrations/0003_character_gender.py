# Generated by Django 5.2 on 2025-04-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character_data', '0002_character_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.CharField(null=True),
        ),
    ]
