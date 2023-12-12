from django.urls import path, include
from render import views

urlpatterns = [
    path('', views.getUsers, name="getUsers"),
    path('register/', views.registerUser, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile,name="getUserProfile"),
    path('profile/update/', views.updateUserProfile,name="updateProfile"),
    path('<str:pk>/', views.getUserById,name="getUser"),
    path('update/<str:pk>/', views.updateUser,name="updateUser"),
    path('delete/<str:pk>/', views.deleteUser,name="deleteUser"),
]