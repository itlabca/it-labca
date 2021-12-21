from django import forms
from core.models import AccesoRemoto, Area, EquipoIT, Mantenimiento, Marca, Modelo, Sucursal, TipoEquipo

class SucursalForm(forms.ModelForm):
    class Meta:
        model=Sucursal
        fields=[
            'nombreSucursal',
            'direccion',
            'gerenteSucursal'
        ]
        labels={
            'nombreSucursal':'Nombre sucursal',
            'direccion':'Direccion',
            'gerenteSucursal':'Gerente sucursal'
        }
        widgets={
            'nombreSucursal':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'direccion':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'gerenteSucursal':forms.TextInput(attrs={'class':'form-control form-control-sm'})
        }

class AreaForm(forms.ModelForm):
    class Meta:
        model=Area
        fields=[
            'nombreArea'
        ]
        labels={
            'nombreArea':'Nombre area'
        }
        widgets={
            'nombreArea':forms.TextInput(attrs={'class':'form-control form-control-sm'})
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields=[
            'nombreMarca'
        ]
        labels={
            'nombreMarca':'Nombre marca'
        }
        widgets={
            'nombreMarca':forms.TextInput(attrs={'class':'form-control form-control-sm'})
        }

class ModeloForm(forms.ModelForm):
    class Meta:
        model=Modelo
        fields=[
            'nombreModelo',
            'marca'
        ]
        labels={
            'nombreModelo':'Nombre Modelo',
            'marca':'Marca'
        }
        widgets={
            'nombreModelo':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'marca':forms.Select(attrs={'class':'form-class form-control-sm'})
        }

class TipoEquipoForm(forms.ModelForm):
    class Meta:
        model=TipoEquipo
        fields=[
            'nombreEquipo'
        ]
        labels={
            'nombreEquipo':'Nombre equipo'
        }
        widgets={
            'nombreEquipo':forms.TextInput(attrs={'class':'form-control form-control-sm'})
        }

class EquipoItForm(forms.ModelForm):
    class Meta:
        model=EquipoIT
        fields=[
            'tipoEquipo',
            'marca',
            'modelo',
            'sucursal',
            'area',
            'fechaIngreso',        
            'observacion',
            'accesoRemoto',
            'aliasEquipo'
        ]
        labels={
            'tipoEquipo':'Tipo equipo',
            'marca':'Marca',
            'modelo':'Modelo',
            'sucursal':'Sucursal',
            'area':'Area',
            'fechaIngreso':'Fecha ingreso',
            'observacion':'Observacion',
            'accesoRemoto':'Aplica acceso remoto',
            'aliasEquipo':'aliasEquipo'
        }
        widgets={
            'tipoEquipo':forms.Select(attrs={'class':'form-class form-control-sm'}),
            'marca':forms.Select(attrs={'class':'form-class form-control-sm'}),
            'modelo':forms.Select(attrs={'class':'form-class form-control-sm'}),
            'sucursal':forms.Select(attrs={'class':'form-class form-control-sm'}),
            'area':forms.Select(attrs={'class':'form-class form-control-sm'}),
            'fechaIngreso':forms.TextInput(attrs={'class':'form-control form-control-sm fecha2'}),
            'observacion':forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':3}), 
            'accesoRemoto':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'aliasEquipo':forms.TextInput(attrs={'class':'form-control form-control-sm'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelo'].queryset=Modelo.objects.none()

        if 'marca' in self.data:
            try:
                marca_id = int(self.data.get('marca'))
                self.fields['modelo'].queryset=Modelo.objects.filter(marca=marca_id).order_by('nombreModelo')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['modelo'].queryset=self.instance.marca.modelo_set.order_by('nombreModelo')
        
class MantenimientoForm(forms.ModelForm):
    class Meta:
        model=Mantenimiento
        fields=[
            'fechaMantenimiento',
            'observacion',
            'idEquipoIt'
        ]
        labels={
            'fechaMantenimiento':'Fecha Mantenimiento',
            'observacion':'Observacion',
            'idEquipoIt':'Equipo IT'
        }
        widgets={
            'fechaMantenimiento':forms.TextInput(attrs={'class':'form-control form-control-sm fecha'}),
            'observacion':forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':3}),
            'idEquipoIt':forms.Select(attrs={'class':'form-control form-control-sm'})
        }

class AccesoRemotoForm(forms.ModelForm):
    class Meta:
        model=AccesoRemoto
        fields=[
            'nombreAcceso',
            'clave',
            'observacion',
            'tipoAcceso',
            'idEquipoIt'
        ]
        labels={
            'nombreAcceso':'Nombre Acceso',
            'clave':'Clave',
            'observacion':'Observacion',
            'tipoAcceso':'Tipo acceso',
            'idEquipoIt':'Equipo IT'
        }
        widgets={
            'nombreAcceso':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'clave':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'observacion':forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':3}),
            'tipoAcceso':forms.Select(attrs={'class':'form-control form-control-sm'}),
            'idEquipoIt':forms.Select(attrs={'class':'form-control form-control-sm'})
        }
        

