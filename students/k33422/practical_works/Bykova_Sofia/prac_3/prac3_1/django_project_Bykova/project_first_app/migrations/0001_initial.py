# Generated by Django 4.1.5 on 2023-01-26 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id_car", models.IntegerField(primary_key=True, serialize=False)),
                ("state_number", models.CharField(max_length=15)),
                ("mark_car", models.CharField(max_length=20)),
                ("model_car", models.CharField(max_length=20)),
                ("color", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Car_owner",
            fields=[
                ("id_owner", models.IntegerField(primary_key=True, serialize=False)),
                ("last_name", models.CharField(max_length=30)),
                ("first_name", models.CharField(max_length=30)),
                ("birth_day", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Ownership",
            fields=[
                (
                    "id_owner_car",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(null=True)),
                (
                    "id_car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="car",
                        to="project_first_app.car",
                    ),
                ),
                (
                    "id_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner",
                        to="project_first_app.car_owner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Driver_license",
            fields=[
                ("id_license", models.IntegerField(primary_key=True, serialize=False)),
                ("license_number", models.CharField(max_length=10)),
                ("category", models.CharField(max_length=10)),
                ("date_of_license", models.DateField()),
                (
                    "id_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="car_owner",
                        to="project_first_app.car_owner",
                    ),
                ),
            ],
        ),
    ]
