from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('mongodb_connection/', views.mongodb_connection, name='mongodb_connection'),
    path('connection/<int:connection_id>/', views.mongodb_connection, name='connection_detail'),
    path('connections/', views.connection_list, name='connection_list'),
    path('connection/<int:connection_id>/delete/', views.connection_delete, name='connection_delete'),

    # path("date/", views.save_the_date, name="save_the_date"),
    # path("date/create/", views.date_create, name="date_create"),
 

]