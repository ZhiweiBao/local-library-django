from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre, Language


def index(request):
    """View function for home page of site."""

    # Generate counts of some main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Number of books which genre is fiction
    num_books_genre_fiction = Book.objects.filter(genre__name__icontains='fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_genre_fiction': num_books_genre_fiction,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # name for the list as a template variable
    template_name = 'catalog/book_list.html'  # Specify the template name/location
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book
