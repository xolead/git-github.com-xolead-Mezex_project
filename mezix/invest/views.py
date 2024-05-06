from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Account, Investor, ViewClient, Status, TypeActiv, FinProduct, ViewActiv, Client, RequestClient, RequestInvestor, MySuggestions, LogStatus



class HomeOutput():
    def __init__(self,id, status, FML, TypeActiv, ViewActiv, sum, name):
        self.id = id
        self.status = status
        self.FML = FML
        self.TypeActiv = TypeActiv
        self.ViewActiv = ViewActiv
        self.sum = sum
        self.name = name
        self.popup = 'popup' + str(self.id)

class OffersOutput():
    def __init__(self, id, FML, status, TypeActiv, ViewActiv, sum):
        self.id = id
        self.status = status
        self.FML = FML
        self.TypeActiv = TypeActiv
        self.ViewActiv = ViewActiv
        self.sum = sum

@login_required
def home(request):
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    RI = RequestInvestor.objects.filter(id_Investor = investor.id)
    offers = []
    for RequestInv in RI:
        offer = RequestClient.objects.filter(id_FinProduct = RequestInv.id_FinProduct, id_TypeActiv = RequestInv.id_TypeActiv, id_ViewClient = RequestInv.id_ViewClient)
        for i in offer:
            if i.sum > RequestInv.min_sum and i.sum < RequestInv.max_sum:
                offers.append(i)
    infos = []
    for i in offers:
        infos.append(HomeOutput(i.id,i.id_Status.NameOfStatus, i.id_Client.FML, i.id_TypeActiv.NameOfTypeActiv, i.id_ViewActiv.NameOfViewActiv, i.sum, i.NameOfActiv))        
    return render(request, 'invest/index.html', {'infos' : infos, 'NameOfInvestor' : investor.name})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

@login_required
def offers(request):
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    RI = RequestInvestor.objects.filter(id_Investor = investor.id)
    infos = []
    for i in RI:
        j = MySuggestions.objects.filter(id_RequestInvestor = i.id)
        for sugg in j:
            infos.append(OffersOutput(id = sugg.id, status= sugg.id_Status.NameOfStatus, sum = sugg.sum, FML = sugg.id_RequestClient.id_Client.FML, ViewActiv = sugg.id_RequestClient.id_ViewActiv.NameOfViewActiv, TypeActiv = sugg.id_RequestClient.id_TypeActiv.NameOfTypeActiv))
            
    return render(request, 'invest/offers.html', {'infos' : infos})

@login_required
def create(request):
    return render(request, 'invest/create.html')

@login_required
def view_files(request):
    return render(request, 'invest/view_files.html')