from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += [
    path('mybooks/', views.loanedBooksByUserListView.as_view(),name='myborrowed'),
]
urlpatterns += [
    path('other/', views.other, name='otherpage'),
]
urlpatterns += [
    path('anime/', views.anime, name='animevost'),
]
urlpatterns += [
    path('wix/', views.wix, name='wixer'),
]
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    path('author/create/',views.AuthorCreate.as_view(),name='author_create'),
    path('author/<int:pk>/update/',views.AuthorUpdate.as_view(),name='author_update'),
    path('author/<int:pk>/delete/',views.AuthorDelete.as_view(),name='author_delete')
    ]
