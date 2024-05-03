from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Account
from .models import ViewClient
from .models import Status
from .models import TypeActiv
from .models import FinProduct
from .models import ViewActiv
from .models import Investor
from .models import Client
from .models import RequestClient
from .models import RequestInvestor
from .models import MySuggestions
from .models import LogStatus

class Output():
    def __init__(self, status, FML, TypeActiv, ViewActiv, sum, name):
        self.status = status
        self.FML = FML
        self.TypeActiv = TypeActiv
        self.ViewActiv = ViewActiv
        self.sum = sum
        self.name = name

@login_required
def home(request):
    clients = []
    clients += Account.objects.filter(login = request.user.username)
    for client in clients:
        investors = []
        investors += Investor.objects.filter(id_Account = client.pk)
        for investor in investors:
            RIS = []
            RIS += RequestInvestor.objects.filter(id_Investor = investor.id)
            for RI in RIS:
                MSS = []    
                MSS += MySuggestions.objects.filter(id_RequestInvestor = RI.id)
                infos = []
                for MS in MSS:
                    RC = MS.id_RequestClient
                    infos.append(Output(MS.id_Status.NameOfStatus, RC.NameOfClient, RC.id_TypeActiv.NameOfTypeActiv, RC.id_ViewActiv.NameOfViewActiv, RC.sum, RC.NameOfActiv))
    return render(request, 'invest/index.html', {'infos' : infos, 'NameOfInvestor' : investor.name})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

@login_required
def offers(request):
    return render(request, 'invest/offers.html')

@login_required
def create(request):
    return render(request, 'invest/create.html')
