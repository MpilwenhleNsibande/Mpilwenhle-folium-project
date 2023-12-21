from django.urls import path, include
from django.contrib import admin  
from . import views

app_name = 'wildlife'

urlpatterns = [
    path('organisations_list/', views.organisation_list, name='organisation_list'),
    path('organisations_detail/<int:pk>/', views.organisation_detail, name='organisation_detail'),
    path('properties_list/', views.property_list, name='property_list'),
    path('properties_detail/<int:pk>/', views.property_detail, name='property_detail'),
    path('map/', views.map_view, name='map_view'),
    path('admin/', admin.site.urls),
    path('', include("wildlife.urls")),
]
