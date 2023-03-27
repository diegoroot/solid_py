# Generated by Django 4.1.6 on 2023-02-20 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "code",
                    models.CharField(
                        db_column="ID", max_length=20, primary_key=True, serialize=False
                    ),
                ),
                ("client", models.CharField(db_column="CLIENT_CODE", max_length=20)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pendiente"),
                            ("ON_PROCESS", "Pagado"),
                            ("SENT", "Rechazado"),
                        ],
                        db_column="STATE",
                        max_length=20,
                    ),
                ),
                ("price", models.IntegerField(db_column="PRICE", null=True)),
                (
                    "created_date",
                    models.DateTimeField(db_column="FECHA_CREA", editable=False),
                ),
                (
                    "updated_date",
                    models.DateTimeField(
                        db_column="FECHA_MODIFICA", editable=False, null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "PAYMENT",
                "db_table": "PAYMENT",
            },
        ),
    ]