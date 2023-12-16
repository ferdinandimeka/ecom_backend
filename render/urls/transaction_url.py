from django.urls import path
from render import views

urlpatterns = [
    path('transactions/', views.getAllTransactions, name="transactions"),
    path('transaction/<str:pk>/', views.getTransaction, name="transaction"),
]