from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('base', views.base, name='base'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='registration'),
    path('registered', views.registered, name='registered'),
    path('addstudent',views.addstudent, name='addstudent'),
    path('editstudent/<id>',views.editstudent, name='editstudent'),
    path('updatestudent/<id>',views.updatestudent, name='updatestudent'),
    path('deletestudent/<id>',views.deletestudent,)

]