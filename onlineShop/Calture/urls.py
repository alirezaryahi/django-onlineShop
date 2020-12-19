from django.urls import path
from .views import Calture_listview, Calture_detailview, Caltute_all, CaltureSearch

urlpatterns = [
    path('arts/all', Caltute_all.as_view()),
    path('arts/<title>', Calture_listview.as_view()),
    path('arts/<efectid>/<name>', Calture_detailview),
    path('searchCalture=<title>', CaltureSearch),

]
