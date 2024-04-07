from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'invest/index.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')