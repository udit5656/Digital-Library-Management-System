import django_tables2 as tables
from django.apps import apps

IssuedBook = apps.get_model('book_issue', 'IssuedBook')


class IssuedBooksTable(tables.Table):
    class Meta:
        model = IssuedBook
        template_name = "django_tables2/bootstrap.html"
        fields = ('created', 'user', 'book', 'return_code', 'deadline')
