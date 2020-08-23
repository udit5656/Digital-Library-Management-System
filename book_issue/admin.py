from django.contrib import admin
from .models import BookIssueCode, IssuedBook, BookReturn

# Register your models here.
admin.site.register(BookIssueCode)
admin.site.register(IssuedBook)
admin.site.register(BookReturn)
