from rest_framework import serializers
from django.contrib.auth.models import User
from simulation.models import Societe_Transfert,Tarif

class UserSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = User
            fields = ('url', 'username', 'email', 'is_staff')


class Societe_TransfertSerializer(serializers.ModelSerializer):
       
        class Meta:
                model = Societe_Transfert
                fields=('nom','adresse','site_web','email','telephone','fax')

class TarifSerializer(serializers.ModelSerializer):
        #societe =Societe_TransfertSerializer(read_only=True)
        societe = serializers.StringRelatedField(read_only=True)
        #societe = serializers.PrimaryKeyRelatedField(read_only=True)
        
        class Meta:
                model = Tarif
                fields =('societe','montant_debut','montant_fin','prix','est_internationnal')
                
                
