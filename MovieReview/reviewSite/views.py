from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Welcome！")
    return render(request, 'reviewSite/index.html')