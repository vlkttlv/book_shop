from django.shortcuts import render
from shop.models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user  # Устанавливаем текущего пользователя как заказчика
            customer = request.user
            total_cost = sum(item['price'] * item['quantity'] for item in cart)
            order.total_cost = total_cost
            order.save()  # Сохраняем заказ

            for item in cart:
                OrderItem.objects.create(order=order,
                                         customer=customer,
                                          book=item['book'],
                                          price=item['price'],
                                          quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
