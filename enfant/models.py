from django.db import models
from individu.models import Individu

# Create your models here.
class Enfant(models.Model):
    nom_mere = models.ForeignKey(Individu, on_delete=models.CASCADE, null=True, related_name='nom_mere')
    nom_enfant = models.ForeignKey(Individu, on_delete=models.CASCADE, null=True, related_name='nom_enfant')
    
    class Meta:
        db_table = "enfants"