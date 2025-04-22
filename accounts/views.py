from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from shop.models import AuthUser

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    template_name = "profile.html"
    model = AuthUser
    context_object_name = "user_profile"

    def get_object(self):
        return self.request.user