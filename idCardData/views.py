from django.shortcuts import render
from .forms import data
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
# Create your views here.


def getdata(request):
    
    form = data()
    if request.method == 'POST':
        form = data(request.POST)
        if form.is_valid():
            students = Student.objects.all()
            flag = True
            for i in students:
                if i.BoardRollNo == request.POST['BoardRollNo']:
                    flag = False
            if flag:
                form.save()
                return render(request, 'icd/sucsess.html')
            else:
                messages.add_message(
                    request, messages.ERROR, 'Data already added with this Roll')
    
    context = {
        'form': form
    }
    
    return render(request, 'icd/getdata.html', context)
