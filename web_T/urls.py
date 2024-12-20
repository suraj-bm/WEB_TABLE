from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_view, name='timetable_view'),
     path('timetable/edit/<int:pk>/', views.edit_timetable, name='edit_timetable'),
     path('timetable/add/', views.add_timetable, name='add_timetable'),
]
