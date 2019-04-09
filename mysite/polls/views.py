from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return(HttpResponse("Hello dude. You're at the polls index.")
