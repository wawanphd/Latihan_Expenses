from django.urls import path

from .views import index, expenses, add_expenses, reports_expenses, save_expenses, delete_expenses, form_update_expenses

urlpatterns = [
    path('', index, name='index'),
    path('expenses/', expenses, name='expenses'),
    path('add-expenses/', add_expenses, name='add-expenses'),
    path('reports-expenses/', reports_expenses, name='reports-expenses'),

    #path untuk save expenses
    path('save_expenses/', save_expenses, name='save_expenses'),

    #path untuk delete expenses
    path('delete_expenses/<int:id>', delete_expenses, name='delete_expenses'),

    #path untuk form edit expenses
    path('form_update_expenses/<int:id>', form_update_expenses, name='form_update_expenses'),

]
