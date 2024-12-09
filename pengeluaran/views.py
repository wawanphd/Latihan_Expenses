from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Expenses


def form_update_expenses(request, id):
    
    #ambil data id yang akan diedit
    data_edit = Expenses.objects.get(id=id)
    
    context ={
        'data_edit':data_edit
    }



    return render(request, 'edit-expenses.html', context)





#fungsi Hapus
def delete_expenses(request, id):
    print(id)

    #cari id yang akan dihapus
    id_hapus = Expenses.objects.get(id=id)

    #lakukan fungsi hapus berdasarkan id_hapus
    id_hapus.delete()


    return redirect('expenses')








def save_expenses(request):
    #Ambil data dari form add-expenses.html
    tanggal = request.POST.get('date')
    kategori = request.POST.get('category')
    deskripsi = request.POST.get('description')
    jumlah = request.POST.get('amount') 

    
    
    #Proses Simpan kedalam database (model expenses =>tabel pengeluaran_expenses)
    # Perintah ini sama dengan perintah insert 
    simpan = Expenses(
        date= tanggal,
        category = kategori,
        description = deskripsi,
        amount = jumlah
    )
    simpan.save()


    return redirect('expenses')

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
