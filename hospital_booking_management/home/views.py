from django.http import HttpResponse
from django.shortcuts import render
from .models import Department,Doctor
from . forms import BookingForm
# Create your views here.

def index(request):

    numbers={
        'fruits':['banana','orange','Kiwi']
    }
    return render(request,'index.html', numbers)

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form={
        'form' : form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    doctors= Doctor.objects.all()
    dict_docs={
        'doctors': doctors
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    return render(request,'contact.html') 

def department(request):
    dept = Department.objects.all()
    dict_dept={
        'dept':dept
    }

    return render(request,'department.html',dict_dept)