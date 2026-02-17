from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_rfp, name='upload_rfp'),
]
