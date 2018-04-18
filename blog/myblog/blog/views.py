from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *


# Create your views here.
def index(request):
    a = Article.objects.all()
    return render(request, 'index.html', {'key1': a})
