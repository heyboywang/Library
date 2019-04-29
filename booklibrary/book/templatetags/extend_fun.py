from django import template
from book.models import Suser,Borrows

register = template.Library()

@register.filter(name="user_info")
def queryuser(uid):
    return Suser.objects.get(pk=uid)

# @register.simple_tag
# def get_borrows():
#     borrowsbooks = Borrows.objects.all()
#     return borrowsbooks
