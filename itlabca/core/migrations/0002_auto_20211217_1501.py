# Generated by Django 3.2.3 on 2021-12-17 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimiento',
            name='usuarioRegistra',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accesoremoto',
            name='idEquipoIt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.equipoit', verbose_name='Equipo IT'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='idEquipoIt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipoit', verbose_name='Equipo IT'),
        ),
    ]
