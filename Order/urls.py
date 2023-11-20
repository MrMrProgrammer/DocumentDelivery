from django.urls import path
from . import views

urlpatterns = [
    path('add-order', views.GetDocument.as_view(), name='add-order'),
    path('show-orders', views.show_order, name='show-orders'),
    path('update_order/<int:order_id>', views.UpdateOrderView.as_view(), name='update_order'),
    path('delete_order/<int:order_id>', views.delete_order, name='delete_order'),

]
