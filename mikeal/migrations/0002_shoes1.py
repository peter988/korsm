# Generated by Django 4.1.1 on 2022-11-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mikeal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="shoes1",
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
                ("disc", models.TextField()),
                ("price", models.TextField()),
                ("image", models.TextField()),
                ("image1", models.TextField()),
                ("cat", models.TextField()),
            ],
        ),
    ]
