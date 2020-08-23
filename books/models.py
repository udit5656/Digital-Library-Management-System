from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)
    publisher_name = models.CharField(max_length=50, blank=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    pub_year = models.PositiveIntegerField()
    books_available = models.IntegerField()

    def __str__(self):
        return self.title

    def check_availability(self):
        if self.books_available > 0:
            return True
        return False

    @classmethod
    def create(cls, title, author_name, pub_year, books_available):
        book = cls(title=title, author_name=author_name, pub_year=pub_year, books_available=books_available)
        return book


