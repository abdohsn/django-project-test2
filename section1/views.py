from django.shortcuts import render
from django.http import HttpResponse
import json
import os


def get_books():
    script_dir = os.path.dirname(__file__)
    books_file_path = os.path.join(script_dir, "db.txt")
    with open(books_file_path) as books_file:
        data = json.load(books_file)
    if not data:
        return None
    return data


# all_books = [{"id": 1, "name": "Book 1", "Description": "description1", "image": "image1"},
#              {"id": 2, "name": "Book 2", "Description": "description2", "image": "image2"},
#              {"id": 3, "name": "Book 3", "Description": "description3", "image": "image3"}]
# with open("db.txt") as f:
#     all_books = json.loads(f.read())


def view_all_books(request):
    context = {
        "all_books": get_books()
    }
    return render(request, "section1/books.html", context)


def view_book(request, book_id):
    for book in get_books():
        if book["id"] == book_id:
            context = {"book": book}
            return render(request, "section1/book.html", context)

