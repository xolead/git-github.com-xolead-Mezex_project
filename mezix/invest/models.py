from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    FML = models.TextField('ФИО', blank = True, null=True)
    phone = models.IntegerField('Телефон', blank= True, null=True)
    
    
class ViewClient(models.Model):
    NameOfViewClient = models.TextField()

    def __str__(self):
        return self.NameOfViewClient
    
class Status(models.Model):
    NameOfStatus = models.TextField()

    def __str__(self):
        return self.NameOfStatus
    

class TypeActiv(models.Model):
    NameOfTypeActiv = models.TextField()

    def __str__(self):
        return self.NameOfTypeActiv
    

class FinProduct(models.Model):
    NameOfFinProduct = models.TextField()

    def __str__(self):
        return self.NameOfFinProduct
    
class ViewActiv(models.Model):
    NameOfViewActiv = models.TextField()

    def __str__(self):
        return self.NameOfViewActiv
    
class Client(models.Model):
    address = models.TextField()
    FML = models.TextField()

    def __str__(self):
        return self.FML
    


class Investor(models.Model):
    id_Account = models.ForeignKey(Account, on_delete = models.CASCADE)
    id_ViewClient = models.ForeignKey(ViewClient, on_delete= models.PROTECT)
    name = models.TextField()

    def __str__(self):
        return self.name
    

class RequestInvestor(models.Model):
    id_FinProduct = models.ForeignKey(FinProduct, on_delete = models.PROTECT)
    id_Investor = models.ForeignKey(Investor, on_delete = models.CASCADE)
    id_Status = models.ForeignKey(Status, on_delete = models.PROTECT)
    id_TypeActiv = models.ForeignKey(TypeActiv, on_delete = models.PROTECT)
    id_ViewActiv = models.ForeignKey(ViewActiv, on_delete = models.PROTECT)
    id_ViewClient = models.ForeignKey(ViewClient, on_delete = models.PROTECT)
    max_sum = models.BigIntegerField()
    max_term = models.BigIntegerField()
    min_sum = models.BigIntegerField()
    min_term = models.BigIntegerField()


class RequestClient(models.Model):
    id_FinProduct = models.ForeignKey(FinProduct, on_delete = models.PROTECT)    
    id_Client = models.ForeignKey(Client, on_delete = models.CASCADE)
    id_Status = models.ForeignKey(Status, on_delete = models.PROTECT)
    id_TypeActiv = models.ForeignKey(TypeActiv, on_delete = models.PROTECT)
    id_ViewActiv = models.ForeignKey(ViewActiv, on_delete = models.PROTECT)
    id_ViewClient = models.ForeignKey(ViewClient, on_delete = models.PROTECT)
    NameOfActiv = models.TextField()
    NameOfClient = models.TextField()
    sum = models.IntegerField()
    term = models.IntegerField()


class MySuggestions(models.Model):
    id_RequestClient = models.ForeignKey(RequestClient, on_delete = models.SET_NULL, null = True)
    id_RequestInvestor = models.ForeignKey(RequestInvestor, on_delete = models.SET_NULL, null = True)
    id_Status = models.ForeignKey(Status, on_delete = models.PROTECT)
    SpecialConditions = models.TextField()
    sum = models.IntegerField()
    term = models.IntegerField()


class LogStatus(models.Model):
    id_Investor = models.ForeignKey(Investor, on_delete = models.CASCADE)
    id_Status = models.ForeignKey(Status, on_delete = models.PROTECT)
    id_MySuggestions = models.ForeignKey(MySuggestions, on_delete = models.SET_NULL, null = True)
    id_Client = models.ForeignKey(Client, on_delete = models.CASCADE)
    time_changes = models.DateTimeField()




