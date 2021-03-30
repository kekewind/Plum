from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashBoard, name="dashboard"),
    path('units/', views.units, name="units"),
    path('user/<str:pk>/', views.person, name="person"),

    #------------ (CREATE URLS) ------------
    path('create_report/', views.createReport, name="create_report"),
   
    #------------ (UPDATE URLS) ------------
    path('update_report/<str:pk>/', views.updateReport, name="update_report"),


    #------------ (UPDATE URLS) ------------
    path('delete_report/<str:pk>/', views.deleteReport, name="delete_report"),

]
