from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (HomePageView,
                    CustomersListView,
                    OrdersListView,
                    OrderDetailView,
                    BookDetailView,
                    BooksListView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('customers', CustomersListView.as_view(), name='orders'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('books', BooksListView.as_view(), name='books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
