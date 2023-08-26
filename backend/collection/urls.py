from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.collect_incident_for_user),
    path("list/", views.get_incidents_for_user)
]
