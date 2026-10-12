from django.urls import path, include, re_path

from django.views.static import serve

from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(),
         name='book_detail'),
    path('authors/', views.author_list,
         name='authors'),
    path('author/<int:pk>', views.author_detail,
         name='author-detail'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), #serve static files when deployed
    path('my_books/', views.LoanedBooksByUserListView.as_view(),
         name='my_books'),
    path('author/create/', views.AuthorCreate.as_view(),
         name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(),
         name='author_update'),
    path('author/<int:pk>/delete/', views.author_delete,
         name='author_delete'),
    path('book/<uuid:pk>/loan/', views.loan_book_librarian, name='loan_book_librarian'),
    path('available/', views.AvailBooksListView.as_view(), name='all_available'),

]
