from django.db import models

# Create your models here.
class Reporting(models.Model):  
    Numero_R =models.AutoField(primary_key=True)
    Date_A =models.DateField(auto_now_add=True,auto_now=True)
    Critére=models.TextField()
    Paramétre=models.CharField(max_length=200)
    taux=models.IntegerField()
    tauxpardefaut=models.IntegerField()
class PlanAction(models.Model):  
    Date_A =models.DateField(auto_now_add=True,auto_now=True)
    Zone=models.CharField(max_length=300)
    cause=models.TextField()
    taux=models.IntegerField()
    delai=models.DateField()
    action_a_faire = models.TextField()
    responsable = models.TextField() 
class Audit(models.Model):
    Numero_A =models.AutoField(primary_key=True)
    Date_A =models.DateField(auto_now_add=True,auto_now=True)
    Zone=models.CharField(max_length=300)
    Auditeur=models.CharField(max_length=200)
    Commentaires=models.TextField()
    choix=[1,0]
    score =models.IntegerField(choices=choix)
    Critére=models.TextField()
    Paramétre=models.CharField(max_length=200)
    taux_respecte =models.IntegerField(null=True)
    #photo=models.ImageField(upload_to=None, height_field=,width_field=)
    #photo-standard=models.ImageField(upload_to=None, height_field=, width_field=)
    reporting = models.OneToOneField(Reporting,on_delete=models.CASCADE,primary_key=True)
    plan_action = models.OneToOneField(PlanAction,on_delete=models.CASCADE,primary_key=True)
class Registre(models.Model):
    Numero_R = models.ForeignKey(Audit,on_delete=models.CASCADE)
    Date_A =models.DateField(auto_now_add=True,auto_now=True)
    Zone=models.CharField(max_length=300)
    Auditeur=models.CharField(max_length=200)
    Taux_respecte =models.IntegerField()
class RegistreReporting5SGeneral(models.Model):
    Numero_R = models.ForeignKey(Reporting,on_delete=models.CASCADE)
    Numero_A =models.IntegerField()
    Date_A =models.DateField(auto_now_add=True,auto_now=True)
    Zone=models.CharField(max_length=300)
    Auditeur=models.CharField(max_length=200)
    Taux_respecte =models.IntegerField() 



    
