# Generated by Django 4.2.5 on 2023-09-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SpendStatistic",
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
                ("name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                (
                    "spend",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("impressions", models.IntegerField(default=0)),
                ("clicks", models.IntegerField(default=0)),
                ("conversion", models.IntegerField(default=0)),
            ],
        ),
    ]
