from django.contrib import admin
from django.urls import path
from django.conf.urls import  include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from mainapp.mainapp import views
from . import views
urlpatterns = [
    path('admin_console',views.admin_console,name="admin_console"),

]
