from django.urls import path, include
from render import views

urlpatterns = [
    path('routes', views.getRoutes, name="Routes"),
    path('', views.getProducts, name="products"),
    path('top/', views.getTopProducts, name="top-products"),
    
    path('create/', views.createProduct, name="create-product"),
    path('upload/', views.uploadImage, name="upload_image"),

    path('<str:pk>/', views.getProduct, name="product"),
    path('update/<str:pk>/',views.updateProduct,name="update_product"),
    path('delete/<str:pk>/',views.deleteProduct,name="delete_product"),
    path('<str:pk>/reviews/', views.createProductReview, name="create-review"),
]