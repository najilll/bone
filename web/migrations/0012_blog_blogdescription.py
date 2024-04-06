# Generated by Django 5.0.3 on 2024-04-05 10:23

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0011_alter_servicedescription_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("slug", models.SlugField()),
                ("sub_title", models.CharField(max_length=150)),
                ("description", models.TextField(max_length=250)),
                ("background_image", models.ImageField(upload_to="baner")),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="BlogDescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="baner/")),
                (
                    "service_description",
                    tinymce.models.HTMLField(blank=True, null=True),
                ),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.blog"
                    ),
                ),
            ],
        ),
    ]