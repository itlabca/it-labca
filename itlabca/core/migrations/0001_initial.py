# Generated by Django 3.2.3 on 2021-12-17 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('idArea', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo area')),
                ('nombreArea', models.CharField(max_length=30, verbose_name='Nombre area')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoIT',
            fields=[
                ('idEquipoIt', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo Equipo IT')),
                ('fechaIngreso', models.DateField(blank=True, null=True, verbose_name='Fecha ingreso')),
                ('observacion', models.TextField(blank=True, null=True, verbose_name='Observacion')),
                ('accesoRemoto', models.BooleanField(default=False, verbose_name='Aplica acceso remoto')),
                ('aliasEquipo', models.TextField(max_length=40, verbose_name='Alias equipo')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.area', verbose_name='Area a asignar')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo marca')),
                ('nombreMarca', models.CharField(max_length=30, verbose_name='Nombre marca')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo sucursal')),
                ('nombreSucursal', models.CharField(max_length=40, verbose_name='Nombre sucursal')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion sucursal')),
                ('gerenteSucursal', models.CharField(max_length=50, verbose_name='Gerente sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEquipo',
            fields=[
                ('idTipoEquipo', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo tipo equipo')),
                ('nombreEquipo', models.CharField(max_length=50, verbose_name='Nombre Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('idModelo', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo modelo')),
                ('nombreModelo', models.CharField(max_length=30, verbose_name='Nombre modelo')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.marca', verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('idMantenimiento', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo mantenimiento')),
                ('fechaMantenimiento', models.DateField(verbose_name='Fecha mantenimiento')),
                ('observacion', models.TextField(verbose_name='Observacion')),
                ('idEquipoIt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.equipoit', verbose_name='Equipo IT')),
            ],
        ),
        migrations.AddField(
            model_name='equipoit',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.marca', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='equipoit',
            name='modelo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.modelo', verbose_name='Modelo'),
        ),
        migrations.AddField(
            model_name='equipoit',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sucursal', verbose_name='Sucursal a asignar'),
        ),
        migrations.AddField(
            model_name='equipoit',
            name='tipoEquipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tipoequipo', verbose_name='Tipo equipo'),
        ),
        migrations.CreateModel(
            name='AccesoRemoto',
            fields=[
                ('idAccesoRemoto', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo acceso remoto')),
                ('nombreAcceso', models.CharField(max_length=30, verbose_name='Nombre Acceso')),
                ('clave', models.CharField(default='-', max_length=30, verbose_name='Clave acceso')),
                ('observacion', models.TextField(verbose_name='Observacion')),
                ('tipoAcceso', models.CharField(choices=[('acceso1', 'TeamViewer'), ('acceso2', 'AnyDesk'), ('acceso3', 'Otro')], max_length=30, verbose_name='Tipo Acceso')),
                ('idEquipoIt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.equipoit', verbose_name='Equipo IT')),
            ],
        ),
    ]
