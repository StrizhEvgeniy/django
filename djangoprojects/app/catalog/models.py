import uuid

from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=20, help_text="Enter genre name")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Enter language name")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Author name")
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Book(models.Model):
    title = models.CharField(max_length=100, help_text="Book title")
    author = models.ManyToManyField(Author)
    summary = models.TextField(help_text="Enter a book description")
    imprint = models.CharField(max_length=10, help_text="Book imprint")
    ISBN = models.CharField(max_length=13, help_text='<a href="#">ISBN number</a>')
    genre = models.ManyToManyField(Genre)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    due_back = models.DateField(null=True,blank=True)

    LOAN_STATUS = (
        ('a','Available'),
        ('r','Reserved'),
        ('o','On Loan')
    )

    status = models.CharField(max_length=1,default='a',choices=LOAN_STATUS)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f"{self.book.title}, {self.id}"




