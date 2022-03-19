from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login')
]

# path: the link after app to show this view
# view.index : refer to the function (view) rendered when request the link main/apppath/viewpath/
