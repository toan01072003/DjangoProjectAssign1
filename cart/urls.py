from django.urls import path
from . import views

urlpatterns = [
    # Example view (replace with your actual views later)
    path('', views.cart_list, name='cart-list'),
]