from django.contrib import admin

from .models import Sucursal, Area, EquipoIT, Mantenimiento, AccesoRemoto

# Register your models here.
class SucursalAdmin(admin.ModelAdmin):
    list_display=('idSucursal','nombreSucursal','direccion')

class AreaAdmin(admin.ModelAdmin):
    list_display=('idArea','nombreArea')

class EquipoItAdmin(admin.ModelAdmin):
    list_display=('idEquipoIt', 'tipoEquipo','marca','sucursal')

class EquipoItAdmin(admin.ModelAdmin):
    list_display=('idEquipoIt','marca')

class MantenimientoAdmin(admin.ModelAdmin):
    list_display=('idMantenimiento','idEquipoIt')

class AccesoRemotoAdmin(admin.ModelAdmin):
    list_display=('idAccesoRemoto','nombreAcceso')

admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(EquipoIT, EquipoItAdmin)
admin.site.register(Mantenimiento, MantenimientoAdmin)
admin.site.register(AccesoRemoto, AccesoRemotoAdmin)