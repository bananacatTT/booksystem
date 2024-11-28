from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'purchase_date', 'cover_image']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="お名前")
    email = forms.EmailField(label="メールアドレス")
    message = forms.CharField(widget=forms.Textarea, label="お問い合わせ内容")