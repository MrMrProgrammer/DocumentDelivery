from django.urls import path
from . import views

urlpatterns = [
    path('show-store', views.show_store, name='show-store'),
    path('add-store', views.StoreRegisterView.as_view(), name='add-store'),
]
