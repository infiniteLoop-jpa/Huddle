from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def huddle_home(request):
    return render(request, 'index.html')

def huddle_group(request):
    return render(request, 'huddle_page.html')
