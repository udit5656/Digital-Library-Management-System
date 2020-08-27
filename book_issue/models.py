import random
import string

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TimeStampModel(models.Model):
    """Model which add creation time"""
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class BookIssueCode(TimeStampModel):
    """Issues code for claiming of book and check for it's validation"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='book')
    code = models.CharField(max_length=6)

    @classmethod
    def create(cls, user, book):
        book_issue_code = cls(user=user, book=book, code=random_string_generator())
        return book_issue_code

    def __str__(self):
        return self.code

    def check_code(self, code):
        if self.code == code:
            return True
        return False

    class Meta:
        permissions = (
            ("can_enter_code_to_issue_book", "can enter code to issue book"),
        )

    # Add a method which checks expiry of code
    # check if same user is asking for same book code again


class IssuedBook(TimeStampModel):
    """Check if code entered while claiming book is right and on update database regarding current state of book"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issued_book_user')
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='issued_book')

    # Add time stamp of issue book
    # Add method to delete BookIssueCode delete after claiming book
    # Add method to update database
    @classmethod
    def create(cls, user, book):
        issued_book = cls(user=user, book=book)
        return issued_book


class BookReturn(TimeStampModel):
    roll_no = models.PositiveIntegerField()
    book = models.CharField(max_length=100)
    # Updates the book avaiablity
    # update book status in user profile
    # deletes book issue and add it to bookhistory
    # update fine
