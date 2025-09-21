from django.urls import path
from . import views

urlpatterns = [
    # This single URL now handles displaying, adding, and deleting expenses.
    path('', views.expense_tracker_view, name='expense_tracker'),
]