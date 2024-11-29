from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'purchase_date', 'cover_image']
        labels = {
            'title': 'タイトル',
            'author': '著者',
            'category': 'カテゴリ',
            'purchase_date': '購入日',
            'cover_image': '表紙画像',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="お名前")
    email = forms.EmailField(label="メールアドレス")
    message = forms.CharField(widget=forms.Textarea, label="お問い合わせ内容")