from django.test import TestCase
from core.models import Item
from django.urls import resolve, reverse
from core.views import (
    contact,
    home,
    index,
    loginPage,
    logoutPage,
    ItemDetailView,
    signupPage
)


class TestUrls(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Items to be created for the tests methods
        Item.objects.create(
            title="Pigs",
            description="A nice good puk meat",
            category="A",
            slug=1
        )

    def test_inde_view_is_resolved(self):
        url = reverse('core:index')
        self.assertEquals(resolve(url).func, index)

    def test_ItemDetail_view_is_resolved(self):
        item = Item.pk
        url = reverse('core:product', kwargs={'slug': item})
        self.assertEquals(resolve(url).func.view_class, ItemDetailView)

    def test_home_view_resolved(self):
        url = reverse('core:home')
        self.assertEquals(resolve(url).func, home)

    def test_contact_view_resolved(self):
        url = reverse('core:contact')
        self.assertEquals(resolve(url).func, contact)

    def test_login_view_resolved(self):
        url = reverse('core:login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_logout_view_resolved(self):
        url = reverse('core:logout')
        self.assertEquals(resolve(url).func, logoutPage)

    def test_signup_view_resolved(self):
        url = reverse('core:signup')
        self.assertEquals(resolve(url).func, signupPage)
