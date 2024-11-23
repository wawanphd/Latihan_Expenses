from django.http import HttpResponse
from django.shortcuts import render
from .models import Expenses



def index(request):

    return render(request, 'home.html')

def expenses(request):
    print('Test Debug')
    data = Expenses.objects.all()
    print(data)

    context = {
        'data':data
    }

    return render(request, 'expenses.html', context)

def add_expenses(request):

    return render(request, 'add-expenses.html')

def reports_expenses(request):
    
    return render(request, 'reports-expenses.html') 
