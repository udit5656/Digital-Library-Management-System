from django.apps import apps
from django_tables2 import tables, TemplateColumn

ACTION = '''<a class="btn btn-primary btn-sm" href="{% url "book_issue:book_return" record.id %}">Return</a>'''
BookIssueCode = apps.get_model('book_issue', 'BookIssueCode')
IssuedBook = apps.get_model('book_issue', 'IssuedBook')
BookReturn = apps.get_model('book_issue', 'BookReturn')


class BookIssueCodeTable(tables.Table):
    class Meta:
        model = BookIssueCode
        template_name = "django_tables2/bootstrap.html"
        fields = ('book', 'code', 'cancel')

    cancel = TemplateColumn(template_name='profiles/tables/book_issue_code_column_update.html')


class IssuedBookTable(tables.Table):

    class Meta:
        model = IssuedBook
        template_name = 'django_tables2/bootstrap.html'
        fields = ('book', 'created', 'due_date', 'book_return_option')

    due_date = TemplateColumn(template_name='profiles/tables/issued_book_column_update.html')
    book_return_option = TemplateColumn(ACTION)


class ReturnedBookTable(tables.Table):
    class Meta:
        model = BookReturn
        template_name = 'django_tables2/bootstrap.html'
        fields = ('book', 'created', 'late_fine')

    late_fine = TemplateColumn(template_name='profiles/tables/returned_book_column_update.html')
