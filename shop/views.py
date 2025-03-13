from django.views.generic import TemplateView
from django.views.generic.list import ListView
from shop.models import Book, Customer, Order


class HomePageView(TemplateView):
    template_name = 'home.html'


class OrdersListView(ListView):
    template_name = "orders.html"
    model = Order
    context_object_name = "orders"


class BookListView(ListView):
    template_name = "books.html"
    model = Book
    context_object_name = "books"
