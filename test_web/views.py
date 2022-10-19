from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def index(req):
    return render(req, "index.html", )
