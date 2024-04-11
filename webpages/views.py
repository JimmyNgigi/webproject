from django.http import HttpResponse
from django.template import loader
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