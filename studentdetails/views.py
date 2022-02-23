from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
def rec_data(request):
    dicta={}
    data = Student.objects.all()
    if request.method == 'POST':
      Firstname= request.POST["fname"]
      Lastname = request.POST["lname"]
      RollNumber=request.POST["Rnum"]
      Class = request.POST["cls"]
      Section = request.POST["sec"]
      College = request.POST["clg"]
    dicta = {
         'First_name': Firstname,'Last_name': Lastname,'Roll_number': RollNumber,'Class':Class,'Section':Section,'College':College
             }
    #print(dicta)
    return render(request,'rec_data.html',context=dicta)
def all(request):
    fulldata = Student.objects.all()
    print(fulldata)

    return render(request,'rec_data.html',{'fulldata' : fulldata})



