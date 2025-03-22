from decimal import Decimal
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


########################### MY MODELS ######################################

class Customer(models.Model):
    """Модель пользователя"""
    id = models.AutoField("ID", primary_key=True, unique=True)
    email = models.EmailField("E-mail", max_length=256)
    hashed_password = models.CharField("Пароль", max_length=256)
    first_name = models.CharField("Имя", max_length=256)
    last_name = models.CharField("Фамилия", max_length=256)
    phone_number = models.CharField("Номер телефона", max_length=20)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('admin', 'Администратор'),
    )

    role = models.CharField("Роль", max_length=20, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f'Пользователь: {self.first_name} {self.last_name}'


class Category(models.Model):
    """Модель категории книги"""
    id = models.AutoField("ID", primary_key=True)
    name = models.CharField("Название категории", max_length=256)

    def __str__(self):
        return f'Категория - {self.name}'


class Book(models.Model):
    """Модель книги"""
    id = models.AutoField("ID", primary_key=True)
    title = models.CharField("Название", max_length=256)
    author = models.CharField("Автор", max_length=256)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 on_delete=models.SET_NULL, null=True)
    description = models.TextField("Описание")
    publishing = models.CharField("Издательство", max_length=128)

    BUNDING_CHOICES = (
        ('soft', 'Мягкий'),
        ('hard', 'Твердый')
    )

    type_of_bunding = models.CharField("Тип переплета", max_length=64, choices=BUNDING_CHOICES)
    stock_quantity = models.PositiveIntegerField("Количество на складе", default=0)
    img = models.ImageField("Изображение", upload_to='img/')

    def __str__(self):
        return f'Книга {self.title} {self.author} (ID {self.id})'


class Comment(models.Model):
    """Модель комментария"""
    id = models.AutoField("ID", primary_key=True)
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="Покупатель", on_delete=models.CASCADE)
    comment_date = models.DateField("Дата комментария", auto_now_add=True)
    comment = models.TextField("Комментарий")

    def __str__(self):
        return f'Комментарий {self.customer} (ID {self.id})'


class Address(models.Model):
    """Модель адреса"""
    id = models.AutoField("ID", unique=True, primary_key=True)
    customer = models.ForeignKey(Customer, verbose_name="Покупатель", on_delete=models.CASCADE)
    country = models.CharField("Страна", max_length=32)
    state = models.CharField("Область", max_length=255, blank=True)
    city = models.CharField("Город", max_length=255)
    street = models.CharField("Улица", max_length=255)
    home = models.CharField("Дом", max_length=10)
    zip_code = models.CharField("Почтовый индекс", max_length=16)

    def __str__(self):
        return f"Адрес: {self.street}, {self.city} {self.home}, {self.country}"


class Order(models.Model):
    """Модель заказа"""
    id = models.AutoField("ID", primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField("Дата создания заказа", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления заказа", auto_now=True)
    total_cost = models.DecimalField("Стоимость заказа", max_digits=10, decimal_places=2)
    order_status = models.BooleanField(default=False)
    payment_method = models.CharField("Способ оплаты", max_length=20)
    is_delivered = models.BooleanField("Доставлен?", default=False)
    address = models.CharField("Адрес доставки", max_length=255)

    def __str__(self):
        return f"Заказ: {self.id} (ID покупателя {self.customer.id})"
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    id = models.AutoField("ID", primary_key=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Book, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


class CartItem(models.Model):
    """Модель товара корзины"""
    id = models.AutoField("ID", primary_key=True)
    customer = models.ForeignKey(Customer, verbose_name="Покупатель", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Количество", default=1)
    price = models.DecimalField(max_digits=50, decimal_places=2, default=0, blank=True)
    order = models.ForeignKey(Order, verbose_name="Заказ", on_delete=models.SET_NULL, null=True, blank=True) # on_delete=models.SET_NULL означает, что если заказ будет удален, ссылка в элементе корзины станет NULL,

    def __str__(self):
        return f"Товар: {self.book.title}, {self.quantity} штук)"







