"""
With the usage of django-allauth app we no longer require this urls.py , we can use the inbuilt views of django-allauth

refer : https://github.com/pennersr/django-allauth/blob/main/allauth/account/urls.py
https://github.com/pennersr/django-allauth/blob/b45cf3b3d1f078bbaca9c1260104b65a61d52a5c/allauth/account/views.py#L143
"""



# from django.urls import reverse_lazy
# from django.views import generic

# from .forms import CustomCreationForm
#
# # Create your views here.
# class SignupPageView(generic.CreateView):
#     form_class = CustomCreationForm
#     success_url = reverse_lazy('login')
#     template_name = "registration/signup.html"

