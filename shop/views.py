from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from cart.forms import CartAddProductForm
from shop.models import CustomUser, Order, Book, Star


class HomePageView(TemplateView):
    template_name = 'home.html'


class CustomersListView(ListView):
    template_name = "customers.html"
    model = CustomUser
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    
class StarsView(LoginRequiredMixin, ListView):
    template_name = "stars.html"
    model = Star
    context_object_name = "stars"

    def get_queryset(self):
        return Star.objects.filter(customer=self.request.user)


class StarsSearchView(LoginRequiredMixin, ListView):
    template_name = "search_stars.html"
    model = Star
    context_object_name = "stars"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Star.objects.filter(
            Q(customer=self.request.user, book__title__icontains=query) |
            Q(customer=self.request.user, book__author__icontains=query)
        ).order_by('book__title')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['search_query'] = query
        return context


class BooksSearchView(ListView):
    template_name = "search_books.html"
    model = Book
    context_object_name = "list_of_all_books"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        ).order_by('title')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['search_query'] = query
        return context
