from django.db import models

class Utilisateur(models.Model):
    nom= models.CharField(max_length=50)
    mot_de_pass= models.CharField(max_length=50)

class AchatDevises(models.Model):
    nom= models.CharField(max_length=50)
    numero=models.CharField(max_length=50)
    devise=models.CharField(max_length=50)
    quantite=models.DecimalField(max_digits=10,decimal_places=2)
    cours=models.DecimalField(max_digits=10, decimal_places=2)
     
