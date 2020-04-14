# Generated by Django 3.0.5 on 2020-04-10 17:14

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
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
                ("name", models.CharField(help_text="Le nom du lieu", max_length=300)),
                (
                    "description",
                    models.TextField(blank=True, help_text="Une description du lieu"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("centre social", "Centre social"),
                            (
                                "securite sociale",
                                "Organisme de sécurité sociale (CAF, CPAM, CARSAT, MSA...)",
                            ),
                            ("tiers lieu", "Tiers-lieu & coworking, FabLab"),
                            ("association", "Association"),
                            ("maison quartier", "Maison de quartier"),
                            (
                                "pimms",
                                "Point Information Médiation Multi Services (PIMMS)",
                            ),
                            ("msap", "Maison de Service au Public (MSAP)"),
                            ("bibliotheque", "Bibliothèque - Médiathèque"),
                            ("formation", "Organisme de formations"),
                            ("pole emploi", "Pôle Emploi"),
                            ("commune", "Commune (Ville, CCAS, Centre Culturel...)"),
                            ("intercommunalite", "Intercommunalité (EPCI)"),
                            (
                                "administration",
                                "Administration - Collectivité territoriale",
                            ),
                            ("departement", "Département (UTPAS, MDS, MDSI, UTAS...)"),
                            ("prefecture", "Préfecture, Sous-Préfecture"),
                            ("autre", "Autre, Inconnu"),
                        ],
                        default="autre",
                        help_text="La typologie du lieu",
                        max_length=32,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("public", "Public"),
                            ("prive", "Privé"),
                            ("public-prive", "Public / Privé"),
                            ("autre", "Autre, Inconnu"),
                        ],
                        default="autre",
                        help_text="Le statut du lieu",
                        max_length=32,
                    ),
                ),
                (
                    "address_raw",
                    models.CharField(help_text="L'adresse complète", max_length=300),
                ),
                (
                    "address_housenumber",
                    models.CharField(
                        blank=True,
                        help_text="Le numéro avec indice de répétition éventuel (bis, ter, A, B)",
                        max_length=5,
                    ),
                ),
                (
                    "address_street",
                    models.CharField(
                        blank=True, help_text="Le nom de la rue", max_length=150
                    ),
                ),
                (
                    "address_postcode",
                    models.CharField(
                        blank=True, help_text="Le code postal", max_length=5
                    ),
                ),
                (
                    "address_citycode",
                    models.CharField(
                        blank=True,
                        help_text="Le code INSEE de la commune",
                        max_length=5,
                    ),
                ),
                (
                    "address_city",
                    models.CharField(
                        blank=True, help_text="Le nom de la commune", max_length=150
                    ),
                ),
                (
                    "latitude",
                    models.FloatField(
                        blank=True,
                        help_text="La latitude (coordonnée géographique)",
                        null=True,
                    ),
                ),
                (
                    "longitude",
                    models.FloatField(
                        blank=True,
                        help_text="La longitude (coordonnée géographique)",
                        null=True,
                    ),
                ),
                (
                    "is_itinerant",
                    models.BooleanField(
                        default=False, help_text="Le lieu est-il itinérant ?"
                    ),
                ),
                (
                    "contact_phone_raw",
                    models.CharField(
                        max_length=300, help_text="Le numéro de téléphone brut"
                    ),
                ),
                (
                    "contact_phone",
                    models.CharField(
                        blank=True,
                        help_text="Le numéro de téléphone",
                        max_length=10,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="le numéro de téléphone doit être au format 0123456789",
                                regex="^[0-9]{10}$",
                            )
                        ],
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(
                        blank=True, help_text="Le courriel", max_length=150
                    ),
                ),
                (
                    "contact_website",
                    models.URLField(
                        blank=True,
                        help_text="L'adresse du site internet",
                        max_length=300,
                    ),
                ),
                (
                    "opening_hours_raw",
                    models.TextField(blank=True, help_text="Les horaires d'ouverture"),
                ),
                (
                    "opening_hours_osm_format",
                    models.CharField(
                        blank=True,
                        help_text="Les horaires d'ouverture au format OpenStreetMap",
                        max_length=150,
                    ),
                ),
                (
                    "has_equipment_wifi",
                    models.BooleanField(default=False, help_text="WiFi"),
                ),
                (
                    "has_equipment_computer",
                    models.BooleanField(default=False, help_text="Ordinateur"),
                ),
                (
                    "has_equipment_scanner",
                    models.BooleanField(default=False, help_text="Scanner"),
                ),
                (
                    "has_equipment_printer",
                    models.BooleanField(default=False, help_text="Imprimante"),
                ),
                (
                    "equipment_other",
                    models.CharField(
                        blank=True,
                        help_text="Autres équipements disponibles",
                        max_length=300,
                    ),
                ),
                (
                    "has_accessibility_hi",
                    models.BooleanField(default=False, help_text="Handicap auditif"),
                ),
                (
                    "has_accessibility_mi",
                    models.BooleanField(default=False, help_text="Handicap moteur"),
                ),
                (
                    "has_accessibility_pi",
                    models.BooleanField(
                        default=False, help_text="Handicap intellectuel ou psychique"
                    ),
                ),
                (
                    "has_accessibility_vi",
                    models.BooleanField(default=False, help_text="Handicap visuel"),
                ),
                (
                    "languages",
                    models.CharField(
                        blank=True, help_text="Langues parlées", max_length=150
                    ),
                ),
                (
                    "payment_methods",
                    models.CharField(
                        blank=True, help_text="Les moyens de paiement", max_length=150
                    ),
                ),
                (
                    "additional_information",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True
                    ),
                ),
                (
                    "osm_node_id",
                    models.IntegerField(
                        blank=True, help_text="OpenStreetMap node id", null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["id"],},
        ),
    ]
