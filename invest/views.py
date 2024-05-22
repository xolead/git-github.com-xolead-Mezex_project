import random as rn
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Account, Investor, ViewClient, Status, TypeActiv, FinProduct, ViewActiv, Client, RequestClient, RequestInvestor, MySuggestions, LogStatus, Answer



class HomeOutput():
    def __init__(self,idAns,id,idInv, status, FML, TypeActiv, ViewActiv, sum, name, activ, bank, pristav):
        self.idAns = idAns
        self.id = id
        self.idInv = idInv
        self.status = status
        self.FML = FML
        self.TypeActiv = TypeActiv
        self.ViewActiv = ViewActiv
        self.sum = sum
        self.name = name
        self.popup = 'popup' + str(self.id)
        self.modal = 'modal' + str(self.id)
        self.activ = activ
        self.bank = bank
        self.pristav = pristav

class OffersOutput():
    def __init__(self, id, FML, status, TypeActiv, ViewActiv, sum, stavka, srok, special):
        self.id = id
        self.status = status
        self.FML = FML
        self.TypeActiv = TypeActiv
        self.ViewActiv = ViewActiv
        self.sum = sum
        self.stavka = stavka
        self.srok = srok
        self.special = special

class CreateOutput():
    def __init__(self, id, FinProduct, TypeActiv, ViewActiv, ViewClient, max_sum, min_sum, max_term, min_term):
        self.id = id
        self.FinProduct = FinProduct
        self.TypeActiv = TypeActiv
        self.ViewActiv = ViewActiv
        self.ViewClient = ViewClient
        self.max_sum = max_sum
        self.min_sum = min_sum
        self.max_term = max_term
        self.min_term = min_term
@login_required
def NewRequest(request):
    idfin = request.POST.get('FinProduct', 4)
    idtypeactiv = request.POST.get("TypeActiv", 7)
    idviewclient = int(request.POST.get('ViewClient', 11))
    idviewactiv = int(request.POST.get('Activ', 11))
    min_summ = request.POST.get('min_summ', 1)
    max_summ = request.POST.get('max_summ', 1)
    max_ter = request.POST.get('max_term', 1)
    min_ter = request.POST.get('min_term', 1)
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    a = RequestInvestor(id_FinProduct = FinProduct.objects.get(pk=idfin), id_TypeActiv=TypeActiv.objects.get(pk=idtypeactiv), id_ViewClient= ViewClient.objects.get(pk=idviewclient), id_ViewActiv=ViewActiv.objects.get(pk=idviewactiv), max_sum=max_summ, min_sum=min_summ, max_term=max_ter, min_term=min_ter, id_Investor=investor, id_Status = Status.objects.get(pk=2))
    a.save()
    return HttpResponseRedirect(reverse('create') )

@login_required
def NewPred(request, idAns):
    stavka = request.POST.get('stavka')
    summ = request.POST.get('summ')
    srok = request.POST.get('srok')  
    special = request.POST.get('special')
    ans = Answer.objects.get(pk=idAns)  
    ans.id_Status = Status.objects.get(pk=3)
    ans.save()
    a = MySuggestions(id_RequestClient = ans.id_RequestClient, id_Investor = Investor.objects.filter(pk=ans.id_Investor.id)[0], id_Status = Status.objects.get(pk=2), sum= summ, stavka = stavka, term = srok, SpecialConditions = special)
    a.save()
    return HttpResponseRedirect(reverse('home') )

@login_required
def home(request):
    '''
    if request.method =='POST':
        stavka = request.POST.get('stavka')
        summ = request.POST.get('summ')
        srok = request.POST.get('srok')
        ansid = request.POST.get('ansid')
        return HttpResponse(f"<h2>Name: {ansid}  Age:</h2>")
    '''
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    RI = RequestInvestor.objects.filter(id_Investor = investor.id)
    offers = []
    for RequestInv in RI:
        offer = RequestClient.objects.filter(id_FinProduct = RequestInv.id_FinProduct, id_TypeActiv = RequestInv.id_TypeActiv, id_ViewClient = RequestInv.id_ViewClient)
        for i in offer:
            a = Answer.objects.filter(id_Investor = investor.id, id_RequestClient = i.id)
            if not(a.exists()):
                ans = Answer(id_Investor = investor, id_RequestClient = i, id_Status = Status.objects.get(pk=2))
                ans.save()
                if i.sum > RequestInv.min_sum and i.sum < RequestInv.max_sum:
                    offers.append(i)
        
            elif a[0].id_Status == Status.objects.get(pk=2):
                if i.sum > RequestInv.min_sum and i.sum < RequestInv.max_sum:
                    offers.append(i)
    infos = set()
    for i in offers:
        infos.add(HomeOutput(Answer.objects.get(id_Investor = investor.id, id_RequestClient=i.id).id,i.id,investor.id,i.id_Status.NameOfStatus, i.id_Client.FML, i.id_TypeActiv.NameOfTypeActiv, i.id_ViewActiv.NameOfViewActiv, i.sum, i.NameOfActiv, i.NameOfActiv, i.bankrotstvo, i.pristav))        
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
    
    j = MySuggestions.objects.filter(id_Investor = investor.id, id_Status = Status.objects.get(pk=2))
    for sugg in j:
        infos.append(OffersOutput(id = sugg.id, status= sugg.id_Status.NameOfStatus, sum = sugg.sum, FML = sugg.id_RequestClient.id_Client.FML, ViewActiv = sugg.id_RequestClient.id_ViewActiv.NameOfViewActiv, TypeActiv = sugg.id_RequestClient.id_TypeActiv.NameOfTypeActiv, stavka = sugg.stavka, srok= sugg.term, special = sugg.SpecialConditions))
    j = MySuggestions.objects.filter(id_Investor = investor.id, id_Status = Status.objects.get(pk=3))
    for sugg in j:
        infos.append(OffersOutput(id = sugg.id, status= sugg.id_Status.NameOfStatus, sum = sugg.sum, FML = sugg.id_RequestClient.id_Client.FML, ViewActiv = sugg.id_RequestClient.id_ViewActiv.NameOfViewActiv, TypeActiv = sugg.id_RequestClient.id_TypeActiv.NameOfTypeActiv, stavka = sugg.stavka, srok= sugg.term, special = sugg.SpecialConditions))
    j = MySuggestions.objects.filter(id_Investor = investor.id, id_Status = Status.objects.get(pk=1))
    for sugg in j:
        infos.append(OffersOutput(id = sugg.id, status= sugg.id_Status.NameOfStatus, sum = sugg.sum, FML = sugg.id_RequestClient.id_Client.FML, ViewActiv = sugg.id_RequestClient.id_ViewActiv.NameOfViewActiv, TypeActiv = sugg.id_RequestClient.id_TypeActiv.NameOfTypeActiv, stavka = sugg.stavka, srok= sugg.term, special = sugg.SpecialConditions))
            
    return render(request, 'invest/offers.html', {'infos' : infos, 'NameOfInvestor' : investor.name})

@login_required
def create(request):
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    RI = RequestInvestor.objects.filter(id_Investor = investor.id)
    infos = []
    for ReqInv in RI:
        infos.append(CreateOutput(id = ReqInv.id, FinProduct = ReqInv.id_FinProduct.NameOfFinProduct, TypeActiv= ReqInv.id_TypeActiv.NameOfTypeActiv, ViewActiv= ReqInv.id_ViewActiv.NameOfViewActiv, ViewClient=ReqInv.id_ViewClient.NameOfViewClient, max_sum = ReqInv.max_sum, min_sum=ReqInv.min_sum, max_term=ReqInv.max_term, min_term=ReqInv.min_term))
    return render(request, 'invest/create.html', {'infos' : infos, 'NameOfInvestor' : investor.name})

@login_required
def CreateDelete(request, id):
    RequestInvestor.objects.filter(pk=id).delete()
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    RI = RequestInvestor.objects.filter(id_Investor = investor.id)
    infos = []
    for ReqInv in RI:
        infos.append(CreateOutput(id = ReqInv.id, FinProduct = ReqInv.id_FinProduct.NameOfFinProduct, TypeActiv= ReqInv.id_TypeActiv.NameOfTypeActiv, ViewActiv= ReqInv.id_ViewActiv.NameOfViewActiv, ViewClient=ReqInv.id_ViewClient.NameOfViewClient, max_sum = ReqInv.max_sum, min_sum=ReqInv.min_sum, max_term=ReqInv.max_term, min_term=ReqInv.min_term))
    return render(request, 'invest/create.html', {'infos' : infos, 'NameOfInvestor' : investor.name})

@login_required
def view_files(request):
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    return render(request, 'invest/view_files.html', {'NameOfInvestor' : investor.name})


@login_required
def HomeDelete(request, id, idInv):
    idClient = RequestClient.objects.get(pk = id)
    idInvestor = Investor.objects.get(pk = idInv)
    dele = Answer.objects.filter(id_RequestClient = idClient.id, id_Investor = idInvestor.id)
    for d in dele:
        d.id_Status = Status.objects.get(pk=1)
        d.save()
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    RI = RequestInvestor.objects.filter(id_Investor = investor.id)
    offers = []
    for RequestInv in RI:
        offer = RequestClient.objects.filter(id_FinProduct = RequestInv.id_FinProduct, id_TypeActiv = RequestInv.id_TypeActiv, id_ViewClient = RequestInv.id_ViewClient)
        for i in offer:
            a = Answer.objects.filter(id_Investor = investor.id, id_RequestClient = i.id)
            if not(a.exists()):
                ans = Answer(id_Investor = investor, id_RequestClient = i, id_Status = Status.objects.get(pk=2))
                ans.save()
                if i.sum > RequestInv.min_sum and i.sum < RequestInv.max_sum:
                    offers.append(i)
        
            elif a[0].id_Status == Status.objects.get(pk=2):
                if i.sum > RequestInv.min_sum and i.sum < RequestInv.max_sum:
                    offers.append(i)
    infos = set()
    for i in offers:
        infos.add(HomeOutput(i.id,investor.id,i.id_Status.NameOfStatus, i.id_Client.FML, i.id_TypeActiv.NameOfTypeActiv, i.id_ViewActiv.NameOfViewActiv, i.sum, i.NameOfActiv))        
    return render(request, 'invest/index.html', {'infos' : infos, 'NameOfInvestor' : investor.name})

@login_required
def SortOffers(request, action):
    clients = Account.objects.filter(username = request.user.username)
    client = clients[0]
    investors = Investor.objects.filter(id_Account = client.id)
    investor = investors[0]
    RI = RequestInvestor.objects.filter(id_Investor = investor.id)
    infos = []
    for i in RI:
        j = MySuggestions.objects.filter(id_RequestInvestor = i.id, id_Status = Status.objects.get(pk=action).id)
        for sugg in j:
            infos.append(OffersOutput(id = sugg.id, status= sugg.id_Status.NameOfStatus, sum = sugg.sum, FML = sugg.id_RequestClient.id_Client.FML, ViewActiv = sugg.id_RequestClient.id_ViewActiv.NameOfViewActiv, TypeActiv = sugg.id_RequestClient.id_TypeActiv.NameOfTypeActiv))
            
    return render(request, 'invest/offers.html', {'infos' : infos})



