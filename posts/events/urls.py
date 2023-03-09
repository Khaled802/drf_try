from django.urls import path

from .views import EventList, EventListAll, GoingView, ImageEventCreate, ImageEventObject 

urlpatterns = [
    path('', EventList.as_view()),
    path('all/', EventListAll.as_view()),
    path('going/', GoingView.as_view()),
    path('images/', ImageEventCreate.as_view()),
    path('images/<int:id>/', ImageEventObject.as_view()),
]