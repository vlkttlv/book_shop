from django.urls import path 
from accounts.views import ProfileView, RegisterView

app_name = 'accounts'


urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
