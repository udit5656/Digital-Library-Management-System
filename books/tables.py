from django_tables2 import tables, TemplateColumn
from .models import Book

ACTION = '''<a href="{%url 'books:detail_view' record.pk %}">{{record.title}}</a>'''


class BookSearchResultTable(tables.Table):
    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
        fields = ('book_name', 'author_name', 'pages')

    book_name = TemplateColumn(ACTION)
