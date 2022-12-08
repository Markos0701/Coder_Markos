from django.db import models
from datetime import*

# Create your models here.

class Miembro(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    afinidad= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField(null=True, blank=True)
    
#models.DateField(null=True)
    