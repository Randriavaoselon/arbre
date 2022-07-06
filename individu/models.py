import uuid
from django.db import models
from datetime import date

# Create your models here.
class Individu(models.Model):

    SEX = (('Homme', 'Homme'),
                 ('Femme', 'Femme'),
                 ('Garçon', 'Garçon'),
                 ('Fille', 'Fille'))
    id = models.AutoField(primary_key=True)
    id_ep = models.PositiveIntegerField(null=True, default=0)
    nom = models.CharField(max_length=90, null=True)
    prenom = models.CharField(max_length=90, null=True)
    date_nais = models.DateField(blank=True, null=True)
    #age = models.IntegerField(null=True, default=0)
    lieu = models.CharField(max_length=30, null=True)
    sex = models.CharField(max_length=30, null=True, choices=SEX)
    def __str__(self):
        return self.nom

    class Meta:
        db_table = "individus"

    @property
    def age(self):
        if(self.date_nais != None):
            age = date.today().year - self.date_nais.year
            return age
