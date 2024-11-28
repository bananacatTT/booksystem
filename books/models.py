from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    purchase_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    borrow_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.borrower_name} borrowed {self.book.title}"
