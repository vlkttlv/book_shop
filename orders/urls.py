from django.urls import path, include
from . import views
app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='order_create'),]