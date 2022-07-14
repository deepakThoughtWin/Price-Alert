"""
  Alert API Routs

"""
from django.contrib import admin
from django.urls import path

# importing views from views.py
from .views import ListAlertAPIView,CreateAlertApiView,AlertDeleteApiView

urlpatterns = [

  path('api/alert/get/',ListAlertAPIView.as_view(),name='alert-get'),
  path('api/alert/create/',CreateAlertApiView.as_view(),name='alert-create'),
  path('api/alert/delete/<int:pk>/',AlertDeleteApiView.as_view(),name='alert-mutation'),
]
