from django.contrib import admin
from .models import *

# Register your models here.

class BorrowsAdmin(admin.ModelAdmin):
    list_display = ['uname','bname','date_borrow','date_retur','statu']
    list_filter = ['uname','bname']
    search_fields = ['uname','bname']


admin.site.register(Suser)
admin.site.register(Book)
admin.site.register(Borrows,BorrowsAdmin)