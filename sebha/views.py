from django.shortcuts import render


def index(request):
    data = {
        "name" : "ahmed",
        "age" : 25
    }
    return render(request, 'app_name/index.html' , data)

# folderOfAppInsideTemplates/filename.html

