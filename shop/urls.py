from django.urls import path
from .views import BookListView, HomePageView, OrdersListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('books', BookListView.as_view(), name='books'),
]