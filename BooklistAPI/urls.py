from django.urls import path
from . import views

urlpatterns = [
    path('book', views.BookView.as_view()),
    # path('books/<int:pk>', views.SingleBookView.as_view()),
]