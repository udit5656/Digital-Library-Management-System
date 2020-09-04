from django.test import SimpleTestCase
from books.views import home, detail_view
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('books:home')
        self.assertEquals(resolve(url).func, home)

    def test_detail_view_url_resolves(self):
        url = reverse('books:detail_view', args=[6])
        self.assertEquals(resolve(url).func, detail_view)
