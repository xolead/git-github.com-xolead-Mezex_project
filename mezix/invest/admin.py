from django.contrib import admin
from .models import Account, Investor, ViewClient, Status, TypeActiv, FinProduct, ViewActiv, Client, RequestClient, RequestInvestor, MySuggestions, LogStatus

admin.site.register(Account)
admin.site.register(Investor)
admin.site.register(ViewClient)
admin.site.register(Status)
admin.site.register(TypeActiv)
admin.site.register(FinProduct)
admin.site.register(ViewActiv)
admin.site.register(Client)
admin.site.register(RequestClient)
admin.site.register(RequestInvestor)
admin.site.register(MySuggestions)
admin.site.register(LogStatus)
