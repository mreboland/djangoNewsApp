from django.urls import reverse_lazy
# We're using django's generic CreateView and telling it to use our CustomUserCreationForm to redirect to login once a user signs up successfully.
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"