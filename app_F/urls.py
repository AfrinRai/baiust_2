from django.urls import path
from .views.fbv_views import book_list

urlpatterns = {
    path('books/', book_list, name='book_list'),
}