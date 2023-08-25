from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import BookingForm
# Create your views here.


def index(request):
    person = {
        'name':'John',
        'age':32,
        'place':'Korrea',
    }
    return render(request,'index.html',person)



def about(request):
    return render(request,'about.html')



def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    

    form = BookingForm()
    dic_form = {
        'form':form

    }
    return render(request,'booking.html',dic_form)
    



def doctors(request):
    doc_details = {
        'docs':Doctors.objects.all()
    }
    return render(request,'doctors.html', doc_details)



def contact(request):
    return render(request,'contact.html')


def department(request):
    dept_details = {
        'dept':Departments.objects.all()
    }
    return render(request,'department.html', dept_details)





