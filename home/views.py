from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='home/index.html')

def courses(request):
    return render(request, template_name='home/courses.html')

def contact(request):
    return render(request, template_name='home/contact.html')

def instructors(request):
    return render(request, template_name='home/instructors.html')

