from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'classroom/homepage.html')

def studentpage(request):
    return render(request, 'classroom/student.html')
    
def profesorpage(request):
    return render(request, 'classroom/profesor.html')
    
def subjectpage(request):
    return render(request, 'classroom/subject.html')
    
def classpage(request):
    return render(request, 'classroom/class.html')