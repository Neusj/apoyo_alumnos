# Generated by Django 2.2.28 on 2024-07-22 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('area_estudiante', '0005_delete_datosalumno'),
        ('area_docente', '0003_auto_20240720_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(default='')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area_estudiante.Estudiante')),
                ('tipo_conducta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='area_estudiante.TipoConducta')),
            ],
        ),
    ]