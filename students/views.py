from unicodedata import name
from django.shortcuts import render

import students
from .models import Student

# Create your views here.


def student(request):

    # to get one object record
        data = Student.objects.get(id=1)
        # data is the object receiving the record object
    
        Students = Student.objects.all()
        # Students receive all objects records of Student model
    
        allData = Students.order_by('-price')
        # allData receive all objects records of that model in the required order
    
        allData = Students.filter(name="Omar")
        # allData receive all objects records of that model that comply with the condition in filter method
    
        allData = Students.filter(name__exact="Omar")
        allData = Students.filter(price__in=[1 , 2])
        # pick from a list 
        allData = Students.filter(price__range=(1 , 2))
        # any value in the range
        allData = Students.filter(name="habashy")
    
        # NOTE: objects.all with or without filters MUST be displayed im HTML by for loop only
    
        studentsCount = str(Students.count())
        # pass count of records in table
    
        sueccessStudents = Students.exclude(name="Diaa")
        #  to exclude specific records by condition
    
        return render(request, 'students/student.html', {"studentsData": allData})
        # studentData is the variable delivering data / allData object to html , you can get to it by {{studentData}}
        # data / allData : is any object to be passed to html file specified , you can pass a plain object

    # folderOfAppInsideTemplates/filename.html
