from django.urls import path

from .views import index_view, add_book_view, book_view, view_book, register_view, login_view, logout_view

urlpatterns = [
    path('', index_view, name='index'),
    path('book/add/', add_book_view, name='add_book'),
    path('book', book_view, name='book'),
    path('book/view/<int:book_id>', view_book, name='book_view'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]

# add_book_view
'''
    urlpatterns = [
        path('', index_view, name='index'),
        path('book/add/', add_book_view, name='add_book_view'), # trailing '/' is required for POST
        path('book', book_view, name='book')
    ]
'''

# 4
'''
    path('book/view/<int:book_id>', book_view, name='book_view')
'''