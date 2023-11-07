from django.urls import path
from . import views

urlpatterns = [
    path('show-store', views.show_store, name='show-store'),
]
