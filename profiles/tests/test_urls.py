from django.test import SimpleTestCase
from django.urls import resolve, reverse

from profiles.views import profile_view, edit_profile


class TestUrls(SimpleTestCase):

    def test_profile_url_resolves(self):
        url = reverse('profiles:profile', args=[120])
        self.assertEquals(resolve(url).func, profile_view)

    def test_edit_profile_url_resolves(self):
        url = reverse('profiles:edit_profile', args=[120])
        self.assertEquals(resolve(url).func, edit_profile)
