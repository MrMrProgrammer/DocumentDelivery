from django.urls import path
from . import views

urlpatterns = [
    path('show-store', views.show_store, name='show-store'),
    path('add-store', views.StoreRegisterView.as_view(), name='add-store'),
    path('delete-store/<int:store_id>', views.delete_store, name='delete-store'),
    path('update-store/<int:store_id>', views.UpdateStoreView.as_view(), name='update-store'),

    path('filter_stores', views.filter_stores, name='filter_stores'),
]
