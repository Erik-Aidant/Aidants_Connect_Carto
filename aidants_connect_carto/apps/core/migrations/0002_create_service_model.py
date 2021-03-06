# Generated by Django 3.0.5 on 2020-04-22 15:22

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("core", "0001_initial_create_place_model")]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=300, verbose_name="Le nom du service"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, verbose_name="Une description du service"
                    ),
                ),
                (
                    "siret",
                    models.CharField(
                        blank=True,
                        max_length=14,
                        verbose_name="Coordonnées juridiques (SIRET)",
                    ),
                ),
                (
                    "target_audience",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("tout public", "Tout public"),
                                ("-25 ans", "-25 ans, Jeune"),
                                ("senior", "Sénior"),
                                ("demandeur emploi", "Demandeur d'emploi"),
                                ("famille", "Famille"),
                                ("allocataire", "Allocataires"),
                            ],
                            max_length=32,
                        ),
                        blank=True,
                        default=list,
                        size=None,
                        verbose_name="Public cible (s'il est différent du public cible du lieu)",
                    ),
                ),
                (
                    "support_access",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("libre", "Accès libre"),
                            ("inscription", "Sur inscription ou rendez-vous"),
                            ("public cible", "Public cible uniquement"),
                            ("adherents", "Adhérents uniquement"),
                        ],
                        max_length=32,
                        verbose_name="Modalités d'accès",
                    ),
                ),
                (
                    "support_mode",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("individuel", "Individuel, Personnalisé"),
                            ("collectif", "Collectif"),
                        ],
                        max_length=32,
                        verbose_name="Modalités d'accompagnement",
                    ),
                ),
                (
                    "schedule_hours_raw",
                    models.TextField(
                        blank=True,
                        help_text="Le mardi de 14h à 18h",
                        verbose_name="Les horaires du service (s'ils sont différents des horaires du lieu)",
                    ),
                ),
                (
                    "schedule_hours_osm_format",
                    models.CharField(
                        blank=True,
                        help_text="Tu 14:00-18:00",
                        max_length=150,
                        verbose_name="Les horaires du service au format OpenStreetMap",
                    ),
                ),
                (
                    "is_free",
                    models.BooleanField(
                        default=True, verbose_name="Le service est-il gratuit ?"
                    ),
                ),
                (
                    "price_details",
                    models.TextField(blank=True, verbose_name="Le details des prix"),
                ),
                (
                    "payment_methods",
                    models.TextField(
                        blank=True,
                        verbose_name="Les moyens de paiements spécifiques à ce service",
                    ),
                ),
                (
                    "has_label_aidants_connect",
                    models.BooleanField(
                        default=False, verbose_name="Labellisé Aidants Connect"
                    ),
                ),
                (
                    "has_label_mfs",
                    models.BooleanField(
                        default=False, verbose_name="Labellisé France Service"
                    ),
                ),
                (
                    "label_other",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Autres labels"
                    ),
                ),
                (
                    "additional_information",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True,
                        null=True,
                        verbose_name="Informations additionnelles stockées au format JSON",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="La date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="La date de dernière modification"
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="core.Place",
                    ),
                ),
            ],
            options={"ordering": ["id"],},
        ),
    ]
