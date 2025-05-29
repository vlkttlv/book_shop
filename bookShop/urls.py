from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
    path("cart/", include("cart.urls")),
    path('', include('shop.urls'))
]
