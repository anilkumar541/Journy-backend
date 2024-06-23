from django.urls import path
from dailyStatus.views import JournyList

urlpatterns = [
    path("daily_status/", JournyList.as_view(), name="journy_list")
]
