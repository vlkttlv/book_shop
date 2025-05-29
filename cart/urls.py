from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='add'),
    path('remove/<int:id>/', views.cart_remove, name='remove'),
]
