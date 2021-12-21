from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):
    idMarca=models.AutoField(primary_key=True, verbose_name="Codigo marca")
    nombreMarca=models.CharField(max_length=30, verbose_name="Nombre marca")

    def __str__(self):
        return '{}'.format(self.nombreMarca)

class Modelo(models.Model):
    idModelo=models.AutoField(primary_key=True, verbose_name="Codigo modelo")
    nombreModelo=models.CharField(max_length=30, verbose_name="Nombre modelo")
    marca=models.ForeignKey(Marca, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Marca")

    def __str__(self):
        return '{}'.format(self.nombreModelo)

class Area(models.Model):
    idArea=models.AutoField(primary_key=True, verbose_name="Codigo area")
    nombreArea=models.CharField(max_length=30, verbose_name="Nombre area")

    def __str__(self):
        return '{}'.format(self.nombreArea)

class Sucursal(models.Model):
    idSucursal=models.AutoField(primary_key=True, verbose_name="Codigo sucursal")
    nombreSucursal=models.CharField(max_length=40, verbose_name="Nombre sucursal")
    direccion=models.CharField(max_length=50, verbose_name="Direccion sucursal")
    gerenteSucursal=models.CharField(max_length=50, verbose_name="Gerente sucursal")

    def __str__(self):
        return '{}'.format(self.nombreSucursal)

class TipoEquipo(models.Model):
    idTipoEquipo=models.AutoField(primary_key=True, verbose_name="Codigo tipo equipo")
    nombreEquipo=models.CharField(max_length=50, verbose_name="Nombre Equipo")

    def __str__(self):
        return '{}'.format(self.nombreEquipo)

class EquipoIT(models.Model):
    idEquipoIt=models.AutoField(primary_key=True, verbose_name="Codigo Equipo IT")
    tipoEquipo=models.ForeignKey(TipoEquipo, verbose_name="Tipo equipo", on_delete=models.SET_NULL, blank=True, null=True)
    marca=models.ForeignKey(Marca, verbose_name="Marca", on_delete=models.SET_NULL, blank=True, null=True)
    modelo=models.ForeignKey(Modelo, verbose_name="Modelo", on_delete=models.SET_NULL, blank=True, null=True)
    sucursal=models.ForeignKey(Sucursal, verbose_name="Sucursal a asignar", on_delete=models.SET_NULL, blank=True, null=True)
    area=models.ForeignKey(Area, verbose_name="Area a asignar", on_delete=models.SET_NULL, blank=True, null=True)
    fechaIngreso=models.DateField(verbose_name="Fecha ingreso", null=True, blank=True)
    observacion=models.TextField(verbose_name="Observacion", null=True, blank=True)
    accesoRemoto=models.BooleanField(verbose_name="Aplica acceso remoto", default=False)
    aliasEquipo=models.TextField(max_length=40, verbose_name="Alias equipo")

    def __str__(self):
        return '{}'.format(self.aliasEquipo)

class Mantenimiento(models.Model):
    idMantenimiento=models.AutoField(primary_key=True, verbose_name="Codigo mantenimiento")
    fechaMantenimiento=models.DateField(verbose_name="Fecha mantenimiento")
    observacion=models.TextField(verbose_name="Observacion")
    idEquipoIt=models.ForeignKey(EquipoIT, verbose_name="Equipo IT", on_delete=models.SET_NULL, blank=True, null=True)
    usuarioRegistra=models.ForeignKey(User, on_delete=models.CASCADE)


class AccesoRemoto(models.Model):
    tipoAccesoChoice=(
        ('acceso1','TeamViewer'),
        ('acceso2','AnyDesk'),
        ('acceso3','Otro')
    )
    idAccesoRemoto=models.AutoField(primary_key=True, verbose_name="Codigo acceso remoto")
    nombreAcceso=models.CharField(max_length=30, verbose_name="Nombre Acceso")
    clave=models.CharField(max_length=30, verbose_name="Clave acceso", default="-")
    observacion=models.TextField(verbose_name="Observacion")
    tipoAcceso=models.CharField(max_length=30, choices=tipoAccesoChoice, verbose_name="Tipo Acceso")
    idEquipoIt=models.ForeignKey(EquipoIT, verbose_name="Equipo IT", on_delete=models.SET_NULL, blank=True, null=True)

    def get_acceso(self):
        return '{}'.format(self.get_tipoAcceso_display())
    