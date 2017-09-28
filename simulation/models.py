from django.db import models

# Create your models here.

class Societe_Transfert(models.Model):
    
    nom =models.CharField('Société de transfert',max_length=20,unique=True)
    adresse = models.CharField(max_length=150)
    site_web=models.URLField()
    email=models.EmailField()
    telephone=models.IntegerField()
    fax=models.IntegerField()

    def __str__(self):
        return self.nom

class Tarif (models.Model):
    societe= models.ForeignKey(Societe_Transfert, related_name='societe', on_delete=models.CASCADE)
    montant_debut = models.IntegerField('Entre')
    montant_fin = models.IntegerField('Et')
    prix= models.IntegerField('Prix')
    est_internationnal=models.BooleanField(default=False)
    

    def __str__(self):
        return "{0} {1} - {2} = {3}".format(self.societe,self.montant_debut,self.montant_fin,self.prix)
    
class Recherche(models.Model):
    pass

    
)    
    
