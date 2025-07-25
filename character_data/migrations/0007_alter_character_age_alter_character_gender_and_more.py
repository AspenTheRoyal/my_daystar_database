# Generated by Django 5.1.3 on 2025-07-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character_data", "0006_character_allosexual_character_orientation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="age",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="character",
            name="gender",
            field=models.CharField(
                choices=[
                    ("Female", "Female"),
                    ("Male", "Male"),
                    ("Non-binary", "Non-binary"),
                    ("Other", "Other"),
                    ("Feminine-aligned", "Feminine-aligned"),
                    ("Masculine-aligned", "Masculine-aligned"),
                ],
                default="Non-binary",
                max_length=255,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="character",
            name="orientation",
            field=models.CharField(default="Straight", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="character",
            name="role",
            field=models.CharField(
                choices=[("Staff", "Staff"), ("Subject", "Subject")],
                default="Subject",
                max_length=255,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="character",
            name="species",
            field=models.CharField(default="Human", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="character",
            name="specificRole",
            field=models.CharField(
                choices=[
                    ("Docile", "Docile"),
                    ("Lahde", "Lahde"),
                    ("Cronus", "Cronus"),
                    ("Halcyon", "Halcyon"),
                    ("Nonviable", "Nonviable"),
                    ("Scientist", "Scientist"),
                    ("Medical Staff", "Medical Staff"),
                    ("Intern", "Intern"),
                ],
                default="Docile",
                max_length=255,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="character",
            name="subjectNumber",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
