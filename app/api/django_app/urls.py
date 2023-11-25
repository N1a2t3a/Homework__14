from django.urls import path
from . import views

urlpatterns = [
    path('quote/<int:quote_id>/', views.view_quote, name='view_quote'),
    path('quote/<int:quote_id>/delete/', views.delete_quote, name='delete_quote'),
    path('authors/', views.author_list, name='author_list'),
    path('author/<int:author_id>/', views.view_author, name='view_author'),
    path('author/<int:author_id>/edit/', views.edit_author, name='edit_author'),
    path('author/<int:author_id>/delete/', views.delete_author, name='delete_author')
]