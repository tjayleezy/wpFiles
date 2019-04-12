from django.shortcuts import render
from django.http import Http404

from .models import academic_dept, academic_class
from .models import file_manager

# Create your views here.
def index(request):
    aca_dep = academic_dept.objects.all()
    context = {'aca_dep': aca_dep}
    return render(request, 'polls/index.html', context)

def dept_detail(request, dept_code):
    print(dept_code)
    try:
        aca_class = academic_class.objects.get(dept_code)
        context = {'aca_class': aca_class}
    except academic_class.DoesNotExist:
        raise Http404("Class does not exist") 
    return render(request, 'polls/EECS.html', context)

def class_detail(request, class_code):
    try:
        files = file_manager.objects.all()
        context = {'file_manager': file_manager}
    except file_manager.DoesNotExist:
        raise Http404("Files does not exist") 
    return render(request, 'polls/file_detail.html', context)
