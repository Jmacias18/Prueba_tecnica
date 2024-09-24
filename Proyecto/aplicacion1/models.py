from django.db import models

# Create your models here.
from django.db import models

class Grupo(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID_Grupo')
    nombre_grupo = models.CharField(max_length=255, db_column='Nombre_Grupo')

    def __str__(self):
        return self.nombre_grupo

class Familia(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID_Familia')
    nombre_familia = models.CharField(max_length=255, db_column='Nombre_Familia')

    def __str__(self):
        return self.nombre_familia

class Producto(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID_producto')
    id_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, db_column='ID_Grupo')
    id_familia = models.ForeignKey(Familia, on_delete=models.CASCADE, db_column='ID_Familia')
    nombre_producto = models.CharField(max_length=255, db_column='Nombre_Producto')

    def __str__(self):
        return self.nombre_producto