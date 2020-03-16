from django.test import TestCase
from django.urls import reverse
from core.models import Item
from django.contrib.auth.models import User


class TestViews(TestCase):
    # Items to be created for the tests methods
    def setUp(self):
        # return super().setUp()
        Item.objects.create(
            title="Pigs",
            description="A nice good puk meat",
            category="A",
            slug=1
        )

        self.user = User.objects.create_user(
            "mike", "mike@gmail.com", password="123321qweewq")

    # Test that the views have the right urls
    def test_home_view_url(self):
        response = self.client.get("/home/")
        self.assertEquals(response.status_code, 200)

    def test_index_view_url(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_signup_view_url(self):
        response = self.client.get("/signup/")
        self.assertEquals(response.status_code, 200)

    def test_login_view_url(self):
        response = self.client.get("/login/")
        self.assertEquals(response.status_code, 200)

    def test_contact_view_url(self):
        response = self.client.get("/contact/")
        self.assertEquals(response.status_code, 200)

    def test_logout_view_url(self):
        response = self.client.get("/logout/")
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, "/login/")

    def test_product_view_url(self):
        item = Item.objects.get(id=1)
        slug = item.slug
        response = self.client.get(f"/product/{slug}/")
        self.assertEquals(response.status_code, 200)

# Test that views have the right the right templates

    def test_index_templateUsed(self):
        response = self.client.get(reverse("core:index"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_home_templateUsed(self):
        response = self.client.get(reverse("core:home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_contact_templateUsed(self):
        response = self.client.get(reverse("core:contact"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')

    def test_login_templateUsed(self):
        response = self.client.get(reverse("core:login"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html')

    def test_logout_templateUsed(self):
        response = self.client.get(reverse("core:logout"))
        self.assertEquals(response.status_code, 302)

    def test_product_templateUsed(self):
        item = Item.objects.get(id=1)
        slug = item.slug
        response = self.client.get(
            reverse("core:product", kwargs={'slug': slug}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/product.html')

    # TESTING LOGING

    def test_login_user_correct_values(self):
        self.data = {
            'username': 'mike',
            'password': "123321qweewq"
        }
        response = self.client.post(
            reverse("core:login"), self.data)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse("core:index"))
        self.assertEquals(self.user.username, 'mike')

    # Testing login with wrong values
    def test_login_user_wrong_values(self):
        self.data = {
            'username': 'mie',
            'password': "121qweewq"
        }
        response = self.client.post(
            reverse("core:login"), self.data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse("core:login"))

    # TESTING SIGNUP VIEW
    def test_signup_view_with_correct_values(self):
        self.data = {
            'username': "Kenny123",
            "email": "kenny123@gmail.com",
            "password1": "12344321qwerrewq",
            "password2": "12344321qwerrewq"
        }
        response = self.client.post(reverse("core:signup"), self.data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse("core:login"))

        # Testing login with new user signedup
        response1 = self.client.post(response.url, {
            'username': "Kenny123", "password": "12344321qwerrewq"})
        self.assertEquals(response1.url, reverse("core:index"))

    # SIGNUP WITH INCORRECT VALUES

    def test_signup_wrong_values(self):
        self.data = {
            'username': "Kenny123",
            "email": "kenny123@gmail.com",
            "password1": "12344werrewq",
            "password2": "12344321qwerrewq"
        }

        response = self.client.post(reverse("core:signup"), self.data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse("core:signup"))

    # Test signup for existing user

    def test_signup_alreadyExisting_user(self):
        self.data = {
            'username': "mike",
            "email": "mike@gmail.com",
            "password1": "12344werrewq",
            "password2": "12344321qwerrewq"
        }

        response = self.client.post(reverse("core:signup"), self.data)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse(
            "core:signup"), status_code=302, target_status_code=200, fetch_redirect_response=True)
