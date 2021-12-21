from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

core_patterns=([
    path('', login_required(views.SucursalList.as_view()), name='sucursal'),
    path('createSucursal', login_required(views.SucursalCreate.as_view()), name='createSucursal'),
    path('updateSucursal/<int:pk>/', login_required(views.SucursalUpdate.as_view()), name='updateSucursal'),
    path('area', login_required(views.AreaList.as_view()), name='area'),
    path('createArea', login_required(views.AreaCreate.as_view()), name='createArea'),
    path('updateArea/<int:pk>', login_required(views.AreaUpdate.as_view()), name='updateArea'),
    path('marca', login_required(views.MarcaList.as_view()), name='marca'),
    path('createMarca', login_required(views.MarcaCreate.as_view()), name='createMarca'),
    path('updateMarca/<int:pk>', login_required(views.MarcaUpdate.as_view()), name='updateMarca'),
    path('modelo', login_required(views.ModeloList.as_view()), name='modelo'),
    path('createModelo', login_required(views.ModeloCreate.as_view()), name='createModelo'),
    path('updateModelo/<int:pk>', login_required(views.ModeloUpdate.as_view()), name='updateModelo'),
    path('tipoEquipo', login_required(views.TipoEquipoList.as_view()), name='tipoEquipo'),
    path('createTipoEquipo', login_required(views.TipoEquipoCreate.as_view()), name='createTipoEquipo'),
    path('updateTipoEquipo/<int:pk>', login_required(views.TipoEquipoUpdate.as_view()), name='updateTipoEquipo'),
    path('equipoIt', login_required(views.EquipoItList.as_view()), name='equipoIt'),
    path('createEquipoIt', login_required(views.EquipoItCreate.as_view()), name='createEquipoIt'),
    path('updateEquipoIt/<int:pk>', login_required(views.EquipoItUpdate.as_view()), name='updateEquipoIt'),

    path('mantenimiento', login_required(views.MantenimientoList.as_view()), name='mantenimiento'),
    path('createMantenimiento/<int:idEquipoIt>', login_required(views.MantenimientoCreate.as_view()), name='createMantenimiento'),
    path('updateMantenimiento/<int:pk>', login_required(views.MantenimientoUpdate.as_view()), name='updateMantenimiento'),

    path('accesoRemoto', login_required(views.AccesoRemotoList.as_view()), name='accesoRemoto'),
    path('createAccesoRemoto/<idEquipoIt>', login_required(views.AccesoRemotoCreate.as_view()), name='createAccesoRemoto'),
    path('updateAccesoRemoto/<int:pk>', login_required(views.AccesoRemotoUpdate.as_view()), name='updateAccesoRemoto'),

    path('ajax/load-modelos', login_required(views.load_modelo), name='load_modelo')

], "core")