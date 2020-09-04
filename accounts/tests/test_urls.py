from django.test import SimpleTestCase
from django.urls import resolve, reverse
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import signup_view


class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_resolves(self):
        url = reverse('accounts:logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_signup_url_resolves(self):
        url = reverse('accounts:signup')
        self.assertEquals(resolve(url).func, signup_view)

    def test_admin_site_login_url_resolves(self):
        url = reverse('accounts:admin_site_login')
        self.assertEquals(resolve(url).func.view_class, LoginView)
