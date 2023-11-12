from django.urls import path
from . import views

urlpatterns = [
    path('add-order', views.GetDocument.as_view(), name='add-order'),
    path('show-orders', views.show_order, name='show-orders')
]
