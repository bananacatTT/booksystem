from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>/add/', views.add_review, name='add_review'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('like/<int:review_id>/', views.toggle_like, name='toggle_like'),
]
