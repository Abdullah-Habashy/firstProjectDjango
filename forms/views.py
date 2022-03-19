from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from forms.models import Login

from .forms import LoginForm

def login(request):
    
    if request.method == 'POST':
        dataform = LoginForm(request.POST)
        if dataform.is_valid():
            dataform.save()
    
    
    # receiving data from the form inside view
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # # checkout received data by printing
    # print(username)
    # print(password)
    # # pass data to target fields
    # data = Login(username=username, password=password)
    # save data
    # data.save()

    # (first is the name of the field in model which will receive the data , second is the name of the variable passed to )

    return render(request, 'forms/emailForm.html' , {'LoginForm':LoginForm})

# folderOfAppInsideTemplates/filename.html


# folderOfAppInsideTemplates/filename.html
