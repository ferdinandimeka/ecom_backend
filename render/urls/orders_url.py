from django.urls import path, include
from render import views

urlpatterns = [
    path('', views.getOrders, name='allorders'),
    path('add/', views.addOrderItems, name="orders-add"),
    path('myorders/', views.getMyOrders, name="myOrders"),
    path('<str:pk>/',views.getOrderById,name="user-order"),
    path('<str:pk>/pay/', views.updateOrderToPaid, name="pay"),
    path('<str:pk>/delete/',views.deleteOrder,name="delete_order"),
]