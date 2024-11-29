from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'books/home.html')

@login_required
def profile(request):
    return render(request, 'books/profile.html', {'user': request.user})

# @login_required
# def book_list(request):
#     books = Book.objects.filter(user=request.user)
#     return render(request, 'books/book_list.html', {'books': books})

def book_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    books = Book.objects.filter(user=request.user) if request.user.is_authenticated else Book.objects.none()
    # books = Book.objects.all()

    if request.user.is_authenticated:
        books = Book.objects.filter(user=request.user)
    else:
        books = Book.objects.none()
    
    if query:
        books = books.filter(
            title__icontains=query
        ) | books.filter(
            author__icontains=query
        ) | books.filter(
            category__name__icontains=query
        )

    if category_id:
        books = books.filter(category_id=category_id)

    categories = Category.objects.all()
    return render(request, 'books/book_list.html', {
        'books': books,
        'categories': categories,
        'query': query,
    })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"お問い合わせ: {name}"
            message = f"送信者: {name} ({email})\n\n{message}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

            messages.success(request, 'お問い合わせを送信しました！')
            return render(request, 'books/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'books/contact.html', {'form': form})

def logout_page(request):
    return render(request, 'books/logout.html')

def logout_view(request):
    logout(request)
    return render(request, 'books/logout_success.html') 

def logout_success(request):
    return render(request, 'books/logout_success.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'books/signup.html', {'form': form})
