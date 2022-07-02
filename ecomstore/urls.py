from django.urls import path, include
from ecomstore import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name="home"),
    path('profile/<str:pk>/', views.Profile, name="profile"),
    path('update-profile/<str:pk>/', views.updateprofile, name="update-profile"),
    path('login/', views.loginPage, name="login"),
    path('product/<str:pk>/', views.product, name="product"),
    path('create-product/', views.createProduct, name="create-product"),
    path('update-product/<str:pk>/', views.updateproduct, name="update-product"),
    path('delete-product/<str:pk>/', views.deleteproduct, name="delete-product"),
    path('register/', views.createProfile, name="create-profile"),
    path('logout/', views.logoutPage, name="logout"),
    path('cart/', views.cartPage, name='cart'),
    path('delete-cart/<str:pk>/', views.deleteCart, name='delete-cart'),
    path('review-product/', views.createReview, name='create-review'),
]
