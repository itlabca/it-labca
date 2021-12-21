from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, UpdateView
from core.forms import AccesoRemotoForm, EquipoItForm, MantenimientoForm, MarcaForm, ModeloForm, SucursalForm, AreaForm, TipoEquipoForm
from django.urls import reverse_lazy
from core.models import AccesoRemoto, Area, EquipoIT, Mantenimiento, Marca, Modelo, Sucursal, TipoEquipo

# Create your views here.
class HomeView(TemplateView):
    template_name="core/index.html"

class SucursalList(ListView):
    model=Sucursal

class SucursalCreate(CreateView):
    model=Sucursal
    form_class=SucursalForm
    success_url=reverse_lazy('core:sucursal')

class SucursalUpdate(UpdateView):
    model=Sucursal
    form_class=SucursalForm
    success_url=reverse_lazy('core:sucursal')

class AreaList(ListView):
    model=Area

class AreaCreate(CreateView):
    model=Area
    form_class=AreaForm
    success_url=reverse_lazy('core:area')

class AreaUpdate(UpdateView):
    model=Area
    form_class=AreaForm
    success_url=reverse_lazy('core:area')

class MarcaList(ListView):
    model=Marca

class MarcaCreate(CreateView):
    model=Marca
    form_class=MarcaForm
    success_url=reverse_lazy('core:marca')

class MarcaUpdate(UpdateView):
    model=Marca
    form_class=MarcaForm
    success_url=reverse_lazy('core:marca')

class ModeloList(ListView):
    model=Modelo

class ModeloCreate(CreateView):
    model=Modelo
    form_class=ModeloForm
    success_url=reverse_lazy('core:modelo')

class ModeloUpdate(UpdateView):
    model=Modelo
    form_class=ModeloForm
    success_url=reverse_lazy('core:modelo')

  
class TipoEquipoList(ListView):
    model=TipoEquipo

class TipoEquipoCreate(CreateView):
    model=TipoEquipo
    form_class=TipoEquipoForm
    success_url=reverse_lazy('core:tipoEquipo')

class TipoEquipoUpdate(UpdateView):
    model=TipoEquipo
    form_class=TipoEquipoForm
    context_object_name='obj'
    success_url=reverse_lazy('core:tipoEquipo')

class EquipoItList(ListView):
    model=EquipoIT

class EquipoItCreate(CreateView):
    model=EquipoIT
    form_class=EquipoItForm
    success_url=reverse_lazy('core:equipoIt')

class EquipoItUpdate(UpdateView):
    model=EquipoIT
    form_class=EquipoItForm
    context_object_name='obj'
    success_url=reverse_lazy('core:equipoIt')

class MantenimientoList(ListView):
    model=Mantenimiento

class MantenimientoCreate(CreateView):
    model=Mantenimiento
    form_class=MantenimientoForm
    success_url=reverse_lazy('core:mantenimiento')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuarioRegistra = self.request.user
        self.object.save()
        return super(MantenimientoCreate, self).form_valid(form)
    
    def get_initial(self):
        initial=super().get_initial()
        initial['idEquipoIt']=self.kwargs['idEquipoIt']
        return initial
    

class MantenimientoUpdate(UpdateView):
    model=Mantenimiento
    form_class=MantenimientoForm
    success_url=reverse_lazy('core:mantenimiento')
    

def load_modelo(request):
    idMarca_id=request.GET.get('marca')
    modelos=Modelo.objects.filter(marca_id=idMarca_id).order_by('nombreModelo')
    return render(request, 'core/modelos.html', {'modelos':modelos})

class AccesoRemotoList(ListView):
    model=AccesoRemoto

class AccesoRemotoCreate(CreateView):
    model=AccesoRemoto
    form_class=AccesoRemotoForm
    success_url=reverse_lazy('core:accesoRemoto')

    def get_initial(self):
        initial=super().get_initial()
        initial['idEquipoIt']=self.kwargs['idEquipoIt']
        return initial

class AccesoRemotoUpdate(UpdateView):
    model=AccesoRemoto
    form_class=AccesoRemotoForm
    success_url=reverse_lazy('core:accesoRemoto')
    context_object_name='obj'


