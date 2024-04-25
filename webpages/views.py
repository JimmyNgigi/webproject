from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from webpages.models import Student
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def webpage(request):
    return HttpResponse("welcome to webpage")
def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())
def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about us.html')
    return HttpResponse(template.render())
def registration(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render())
def deletestudent(request,id):
    deletestudent= Student.objects.get(id=id)
    deletestudent.delete()
    return redirect('registered')
def registered(request):
    mydata=Student.objects.all()
    context={'data':mydata}
    return render(request, 'registered clients.html', context)



@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
        formfname = request.POST.get('Fname')
        formlname = request.POST.get('Lname')
        formemail = request.POST.get('email')
        formage = request.POST.get('age')
        print(formfname, formlname, formemail,formage)
        obj1 = Student(FirstName=formfname, LastName=formlname,Email=formemail,Age=formage)
        obj1.save()
        #fetch the student data to be displayed
    mydata = Student.objects.all()
    context = {'data': mydata}
    return render(request, 'registered clients.html', context)

def editstudent(request,id):
    data = Student.objects.get(id=id)
    context = {'data':data}
    return render(request, 'editstudent', context)


def editstudent(request, id):
    if request.method == 'POST':
        fname = request.POST.get['fname']
        lname = request.POST.get['lname']
        email = request.POST.get['email']
        age = request.POST.get['age']
        print(fname, lname, email,age)

        editstudent = Student.objects.get(id=id)
        editstudent.studentfirstname = fname
        editstudent.studentlastname = lname
        editstudent.studentemail = email
        editstudent.studenteage = age

