from django.contrib import admin
from .models import BookIssueCode, IssuedBook, BookReturn,TimeStampModel,LateFine

# Register your models here.
admin.site.register(BookIssueCode)
admin.site.register(IssuedBook)
admin.site.register(BookReturn)
admin.site.register(LateFine)