from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
# from .forms import CustomCreationForm # With django-authall this is no longer required
# from .views import SignupPageView  # With django-authall this is no longer required


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='vk2',
            email='vk2@email.com',
            password='testpass123'
        )

        self.assertEqual(user.username, "vk2")
        self.assertEqual(user.email, 'vk2@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):  # new

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse("account_signup") # previously 'signup' now with django-allauth it is "account_signup" refer allauth doc https://github.com/pennersr/django-allauth/blob/main/allauth/account/urls.py
        self.response = self.client.get(url)


    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html") # before it was "registration/signup.html"
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")


    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

    # No longer required test cases

    # def test_signup_form(self):  # new
    #     form = self.response.context.get("form")
    #     self.assertIsInstance(form, CustomCreationForm)
    #     self.assertContains(self.response, "csrfmiddlewaretoken")
    #

    # def test_signup_view(self):  # new
    #     view = resolve("/accounts/signup/")
    #     self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
