from django.test import TestCase

from aidants_connect_carto.apps.core import stats
from aidants_connect_carto.apps.core.models import DataSource, DataSet, Place, Service


class StatsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        data_source_1 = DataSource.objects.create(name="Region Test", type="region")
        data_set_1 = DataSet.objects.create(
            name="Lieux EPN 2019", data_source_id=data_source_1.id
        )
        data_set_2 = DataSet.objects.create(
            name="Tiers Lieux", data_source_id=data_source_1.id
        )
        place_1 = Place.objects.create(
            name="Lieu Test 1",
            address_region_name="Auvergne-Rhône-Alpes",
            data_set_id=data_set_1.id,
        )
        Service.objects.create(name="Stockage numérique sécurisé", place_id=place_1.id)
        place_2 = Place.objects.create(
            name="Lieu Test 2",
            address_region_name="Île-de-France",
            data_set_id=data_set_2.id,
        )
        Service.objects.create(
            name="Accès à un équipement informatique", place_id=place_2.id
        )
        Service.objects.create(name="Stockage numérique sécurisé", place_id=place_2.id)

    def test_data_source_model_stats(self):
        data_source_model_stats = stats.get_data_source_model_stats()
        self.assertIsInstance(data_source_model_stats, dict)
        self.assertEqual(data_source_model_stats["data_source_count"], 1)

    def test_data_set_model_stats(self):
        data_set_model_stats = stats.get_data_set_model_stats()
        self.assertIsInstance(data_set_model_stats, dict)
        self.assertEqual(data_set_model_stats["data_set_count"], 2)

    def test_place_model_stats(self):
        place_model_stats = stats.get_place_model_stats()
        self.assertIsInstance(place_model_stats, dict)
        self.assertEqual(place_model_stats["place_count"], 2)
        self.assertEqual(place_model_stats["place_with_service_count"], 2)
        self.assertEqual(
            len(place_model_stats["place_address_region_name_aggregation"]), 2
        )
        self.assertEqual(
            place_model_stats["place_address_region_name_aggregation"][0][
                "address_region_name"
            ],
            "Auvergne-Rhône-Alpes",
        )

    def test_service_model_stats(self):
        service_model_stats = stats.get_service_model_stats()
        self.assertIsInstance(service_model_stats, dict)
        self.assertEqual(service_model_stats["service_count"], 3)
        self.assertEqual(len(service_model_stats["service_name_aggregation"]), 7)
        self.assertEqual(
            service_model_stats["service_name_aggregation"][0]["name"],
            "Stockage numérique sécurisé",
        )

    def test_model_stats(self):
        model_stats = stats.get_model_stats()
        self.assertIsInstance(model_stats, dict)
        self.assertEqual(model_stats["data_source_count"], 1)
        self.assertEqual(model_stats["data_set_count"], 2)
        self.assertEqual(model_stats["place_count"], 2)
        self.assertEqual(model_stats["service_count"], 3)
