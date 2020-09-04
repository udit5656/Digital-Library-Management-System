from django.test import SimpleTestCase
from django.urls import reverse, resolve
from book_issue.views import issue, book_return, cancel_request


class TestUrls(SimpleTestCase):

    def test_issue_url_resolves(self):
        url = reverse('book_issue:issue', args=[5])
        self.assertEquals(resolve(url).func, issue)

    def test_book_return_url_resolves(self):
        url = reverse('book_issue:book_return', args=[5])
        self.assertEquals(resolve(url).func, book_return)

    def test_cancel_request_url_resolves(self):
        url = reverse('book_issue:cancel_request', args=[5])
        self.assertEquals(resolve(url).func, cancel_request)