from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from shop.models import CustomUser, CartItem, Comment, Book, Order, Star, Category, OrderItem

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Права доступа', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2',
                'is_staff', 'is_active'
            )}
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Star)
admin.site.register(OrderItem)