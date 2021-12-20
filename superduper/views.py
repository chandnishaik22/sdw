
from django.shortcuts import render,redirect

from .models import superduper

from django.views.decorators.http import require_GET, require_POST


# Create your views here.
@require_POST
def myView(request):
   return redirect('https://api.github.com/search/users?q=python&page=2')
   print(request,POST['stargazers_count'])
