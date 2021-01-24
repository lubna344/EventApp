from django.urls import path, include
from event_app import views

urlpatterns = [
    path('event_app/', views.index, name="event_app"),
    path('del/<id>', views.remove, name="delete"),   
]