from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
def rec_data(request):
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

    s=Student()
    s.Firstname = Firstname
    s.Lastname = Lastname
    s.save()
    all_students = Student.objects.all()
    context = dict()
    context['all_students'] = all_students
    return render(request,'rec_data.html',context=context)
def all(request):
    fulldata = Student.objects.all()
   # print(fulldata)

    return render(request,'rec_data.html',{'fulldata' : fulldata})



