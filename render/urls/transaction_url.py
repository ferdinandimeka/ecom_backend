from django.urls import path
from render import views

urlpatterns = [
    path('', views.getAllTransactions, name="transactions"),
    path('<str:pk>/', views.getTransaction, name="transaction"),
]