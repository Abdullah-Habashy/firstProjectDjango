from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    
    def __str__(self):
        # pass this (self) class
        return self.username
        # pass here the key you want its value to be displayed in admin pane (rename column)
    class Meta:
        verbose_name = "Login"
    # name of Table in admin panel can be changed here(rename table)
