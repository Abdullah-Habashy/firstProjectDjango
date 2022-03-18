from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product/', views.product, name='product')]


# path: the link after app to show this view
# view.index : refer to the function (view) rendered when request the link main/apppath/viewpath/
