from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="home"),   # ^$
    re_path(r'^books/$', views.BookListView.as_view(), name="books"),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name="book-detail"),
    re_path(r'^mybooks/$', views.BookinstanceBorrowedListView.as_view(), name="borrowed")
]




