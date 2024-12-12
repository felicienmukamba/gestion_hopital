# Generated by Django 5.1.1 on 2024-12-06 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hospial", "0003_produit_libelle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lignecommande",
            name="commande",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lignescommande",
                to="hospial.commande",
            ),
        ),
    ]
