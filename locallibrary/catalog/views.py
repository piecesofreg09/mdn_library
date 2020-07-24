from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()
    num_books_contains_ay = Book.objects.filter(title__icontains='ay').count()
    books_contains_ay = Book.objects.filter(title__icontains='ay')

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_ay': num_books_contains_ay,
        'books_ay': books_contains_ay,
        'num_v': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
class BookListView(generic.ListView):
    model = Book
    # your own name for the list as a template variable
    #context_object_name = 'my_book_list'
    # Get 5 books containing the title war
    #queryset = Book.objects.filter(title__icontains='war')[:5] 
    # Specify your own template name/location
    #template_name = 'books/my_arbitrary_template_name_list.html' 
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author