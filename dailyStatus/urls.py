from django.urls import path
from . import views

urlpatterns = [
    path("daily_status/", views.JournyList.as_view(), name="journy_list"),
    path("all_journey/", views.AllJournyList.as_view(), name="all_journey")
]
