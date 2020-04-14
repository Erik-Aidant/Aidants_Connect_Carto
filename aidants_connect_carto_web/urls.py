from django.urls import path

from aidants_connect_carto_web import views


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("lieux", views.place_list, name="place-list"),
    path("lieux/nouveau", views.place_create, name="place-create"),
    path("lieux/<int:place_id>", views.place_details, name="place-details"),
    path("lieux/<int:place_id>/modifier", views.place_update, name="place-update"),
    path(
        "lieux/<int:place_id>/services/nouveau",
        views.service_create,
        name="service-create",
    ),
    path(
        "lieux/<int:place_id>/services/<int:service_id>/modifier",
        views.service_update,
        name="service-update",
    ),
]
