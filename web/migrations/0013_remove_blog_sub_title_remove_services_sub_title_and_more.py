# Generated by Django 5.0.3 on 2024-04-05 10:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0012_blog_blogdescription"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="sub_title",
        ),
        migrations.RemoveField(
            model_name="services",
            name="sub_title",
        ),
        migrations.AddField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]