from django.urls import path
from .views import upload_rfp

urlpatterns = [
    path("", upload_rfp, name="upload_rfp"),
]
