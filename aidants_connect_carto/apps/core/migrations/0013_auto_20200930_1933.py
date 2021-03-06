# Generated by Django 3.0.5 on 2020-09-30 17:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_auto_20200929_1210"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="labels",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True,
                    choices=[
                        ("APTIC", "APTIC"),
                        ("Aidants Connect", "Aidants Connect"),
                        ("France Services", "France Services"),
                        ("Fabriques de Territoire", "Fabriques de Territoire"),
                    ],
                    max_length=150,
                ),
                blank=True,
                default=list,
                help_text="Aidants Connect, France Services, APTIC, ...",
                size=None,
                verbose_name="Label(s)",
            ),
        ),
        migrations.AddField(
            model_name="place",
            name="labels_raw",
            field=models.TextField(blank=True, verbose_name="Label(s) brut"),
        ),
    ]
