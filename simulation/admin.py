from django.contrib import admin

# Register your models here.
from .models import Societe_Transfert,Tarif

admin.site.register(Societe_Transfert)
admin.site.register(Tarif)
