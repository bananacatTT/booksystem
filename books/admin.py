from django.contrib import admin
from .models import Book, BorrowRecord, Category

admin.site.register(Book)
admin.site.register(BorrowRecord)
admin.site.register(Category)
