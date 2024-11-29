from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('new/', views.book_create, name='book_create'),
    path('<int:pk>/edit/', views.book_update, name='book_update'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('contact/', views.contact, name='contact'),
    path('login/', LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='logout_success'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('logout-success/', views.logout_success, name='logout_success'),
    path('signup/', views.signup, name='signup'),
]
