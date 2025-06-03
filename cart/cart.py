from decimal import Decimal
from django.conf import settings
from shop.models import Book

class Cart(object): # Класс для управления корзиной покупок, хранящейся в сессии Django.

    # Инициализирует корзину из сессии пользователя. 
    # Если корзина не существует — создаёт новую пустую.
    def __init__(self, request): 
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавляет товар в корзину или обновляет его количество.
    def add(self, product, quantity=1, update_quantity=False): 
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self): # Сохраняет изменения в корзине в сессию.
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product): # Удаляет товар из корзины.
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Итератор по элементам корзины.
    # Добавляет в каждый элемент объект Book и вычисляет полную стоимость товара.
    def __iter__(self): 
        product_ids = self.cart.keys()
        products = Book.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['book'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self): # Возвращает общее количество товаров в корзине.
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self): # Возвращает общую сумму всех товаров в корзине.
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self): # Полностью очищает корзину в сессии.
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
