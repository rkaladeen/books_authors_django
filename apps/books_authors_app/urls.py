from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('add-book/', views.add_book),
  path('authors/', views.authors),
  path('add-author/', views.add_author),
  path('books/<int:bkid>/', views.book_info),
  path('add-author-to-book/<int:bkid>/', views.add_author_to_book),
  path('authors/<int:atid>/', views.author_info),
  path('add-book-to-author/<int:atid>/', views.add_book_to_author),
]