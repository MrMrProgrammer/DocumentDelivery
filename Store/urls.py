from django.urls import path
from . import views

urlpatterns = [
    path('save-store', views.show_store, name='show-store'),
]
