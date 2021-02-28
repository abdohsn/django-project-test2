from django.urls import path

import section1.views as section1_views

urlpatterns = [
    path('books', section1_views.view_all_books),
    path('book/<int:book_id>', section1_views.view_book)
]