# Generated by Django 5.0.3 on 2024-04-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0003_remove_services_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="slug",
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
