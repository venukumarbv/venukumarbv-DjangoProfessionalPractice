from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomCreationForm

# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

