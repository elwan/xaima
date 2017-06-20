from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import  viewsets
from .serializers import UserSerializer,Societe_TransfertSerializer,TarifSerializer
from simulation.models import Tarif,Societe_Transfert
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Societe_TransfertList(generics.ListCreateAPIView):
    queryset=Societe_Transfert.objects.all()
    serializer_class = Societe_TransfertSerializer

class TarifList(generics.ListCreateAPIView):
    queryset= Tarif.objects.all()
    serializer_class = TarifSerializer

