from django import template
from datetime import date

register = template.Library()


@register.simple_tag
def check_deadline(deadline):
    if date.today() <= deadline:
        return "True"
    return "False"
