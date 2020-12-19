from django.urls import path
from .views import stationery_listview, stationery_detailview, stationery_all, StationerySearch

urlpatterns = [
    path('stationeries/all', stationery_all.as_view()),
    path('stationeries/<title>', stationery_listview.as_view()),
    path('stationeries/<stationeryid>/<name>', stationery_detailview),
    path('searchStationery=<title>', StationerySearch),
]
