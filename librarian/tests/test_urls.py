from django.test import SimpleTestCase
from django.urls import resolve, reverse

from librarian.views import home, search_view, book_issue_request_search_view, issued_books_view


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('librarian:home')
        self.assertEquals(resolve(url).func, home)

    def test_search_url_resolves(self):
        url = reverse('librarian:search')
        self.assertEquals(resolve(url).func, search_view)

    def test_search_result_url_resolves(self):
        url = reverse('librarian:search_result', args=["testing"])
        self.assertEquals(resolve(url).func, book_issue_request_search_view)

    def test_issued_books_url_resolves(self):
        url = reverse('librarian:issued_books')
        self.assertEquals(resolve(url).func, issued_books_view)
