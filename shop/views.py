from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from shop.models import Customer, Order, Book


class HomePageView(TemplateView):
    template_name = 'home.html'


class CustomersListView(ListView):
    template_name = "customers.html"
    model = Customer
    context_object_name = "list_of_all_customers"


class OrdersListView(ListView):
    template_name = "orders.html"
    model = Order
    context_object_name = "list_of_all_orders"


class OrderDetailView(DetailView):
    template_name = "order_detail.html"
    model = Order
    context_object_name = "order"


class BooksListView(ListView):
    template_name = "books.html"
    model = Book
    context_object_name = "list_of_all_books"


class BookDetailView(DetailView):
    template_name = "book_detail.html"
    model = Book
    context_object_name = "book"