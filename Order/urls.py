from django.urls import path
from . import views

urlpatterns = [
    path('get-doc', views.GetDocument.as_view(), name='get-doc'),
]
