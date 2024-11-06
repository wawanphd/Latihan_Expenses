from django.urls import path

from .views import index, expenses, add_expenses, reports_expenses

urlpatterns = [
    path('', index, name='index'),
    path('expenses/', expenses, name='expenses'),
    path('add-expenses/', add_expenses, name='add-expenses'),
    path('reports-expenses/', reports_expenses, name='reports-expenses'),
]
