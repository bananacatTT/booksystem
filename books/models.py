from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='カテゴリ')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='タイトル')
    author = models.CharField(max_length=100, verbose_name='著者')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="カテゴリ")
    purchase_date = models.DateField(verbose_name='購入日')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True, verbose_name='表紙画像')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='登録者')
    

    def __str__(self):
        return self.title
    
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    borrow_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.borrower_name} borrowed {self.book.title}"
    