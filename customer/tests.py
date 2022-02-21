from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
import customer
from customer.views import alogin, cdisplay, contactdisplay, home, alogin, Catering
from customer.models import Customer, catering
from django.contrib.auth.models import User
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_resolve_to_home(self):

            url = reverse("home")

            resolver = resolve(url)

            self.assertEquals(resolver.func,home)



    def test_resolve_to_login(self):

            url = reverse("login")

            resolver = resolve(url)

            self.assertEquals(resolver.func,alogin)

    def test_resolve_to_cdisplay(self):

            url = reverse("customer")

            resolver = resolve(url)

            self.assertEquals(resolver.func,cdisplay)

    def test_resolve_to_catering(self):

            url = reverse("catering")

            resolver = resolve(url)

            self.assertEquals(resolver.func,Catering)
    

    def test_resolve_to_contactdisplay(self):

            url = reverse("messages")

            resolver = resolve(url)

            self.assertEquals(resolver.func,contactdisplay)