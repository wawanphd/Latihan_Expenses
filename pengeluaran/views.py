from django.http import HttpResponse
from django.shortcuts import render




def index(request):

    return render(request, 'home.html')

def expenses(request):

    return render(request, 'expenses.html')

def add_expenses(request):

    return render(request, 'add-expenses.html')

def reports_expenses(request):
    
    return render(request, 'reports-expenses.html') 

