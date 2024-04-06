# Generated by Django 5.0.2 on 2024-04-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0014_remove_blog_background_image_blog_img_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                ("name", models.CharField(max_length=250)),
                ("description", models.TextField()),
                ("profile_image", models.ImageField(upload_to="testimonial/")),
                ("is_active", models.BooleanField(default=True)),
                ("position", models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name="banner",
            name="sub_title",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="banner",
            name="title",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="services",
            name="description",
            field=models.TextField(),
        ),
    ]
