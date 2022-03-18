from datetime import date, datetime

from django.db import models

# Create your models here.


class Student(models.Model):
    # here is table name which is a model
    
    
#here is some data needed in admin panel design-------
    departments = [
        # list to be added inside choises of department column
        ('choice1', 'primary'),
        # first word is the name of choice & second word is what will be displayed in admin panel
        ('choice2', 'Preparatory'),
        ('choice3', 'Secondary'),
    ]


# here we will write names of columns--------:

    name = models.CharField(max_length=50, default='habashy')
    # default : to add default value
    content = models.TextField(null=True, blank=True)
    # null & blank : to allow saving without value
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Value in EGP')
    # verbose_name : to change name of field an ADMIN
    department = models.CharField(
        max_length=50, default='hababshy', choices=departments)
    # Choices : to add value in admin panel by selection from choices
    image = models.ImageField(upload_to=' photos/%y/%m/%d' )
    # create folders sequencly : year/month/day 
    # active = models.BooleanField(default=True)
    # to add check box bbolean field 
    date = models.DateField()
    time = models.TimeField(default= datetime.now)
    createdIn = models.DateTimeField(default= datetime.now)
    # to use date in python you need to import : 
    # from datetime import date, datetime
    
    

    def __str__(self):
        # pass this (self) class
        return self.name
        # pass here the key you want its value to be displayed in admin panel (rename records odjects by name column value )


# here we pass meta data about model -----
    class Meta:
        verbose_name = "Student"
        # name of Table in DB can be changed here
        ordering = ['name']
        # order records ascending
        ordering = ['-price']
        # order price descending
        # Note : the second order override the first and so on


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    # pass here the key you want its value to be displayed in admin panem


