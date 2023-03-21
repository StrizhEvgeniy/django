from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *


def index(request):
    books_count = Book.objects.count()    # select count(*) from Book
    authors_count = Author.objects.count()
    books_instance_count = BookInstance.objects.count()
    books_instance_available_count = BookInstance.objects.filter(status__exact='a').count()

    visits_count = request.session.get('visits_count', 0)

    request.session['visits_count'] = visits_count + 1

    return render(
        request,
        'index.html',
        context={
            'books_count': books_count,
            'authors_count': authors_count,
            'books_instance_count': books_instance_count,
            'books_instance_available_count': books_instance_available_count,
            'visits_count': visits_count,
        }
    )


class BookListView(generic.ListView):

    model = Book

    paginate_by = 8


class BookDetailView(generic.DetailView):

    model = Book

    paginate_by = 4


class BookinstanceBorrowedListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    paginate_by = 5
    template_name = 'catalog/bookinstance_borrowed.html'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


