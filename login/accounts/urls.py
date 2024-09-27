from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path('predict/', views.PredictFraudView.as_view(), name='predict-fraud'),
    path('transaction/', views.create_transaction, name='create_transaction'),
    path('transactions/', views.transactions, name='get_transactions'),
    path('transactions/<int:pk>/', views.transactions, name='delete_transaction'),
]