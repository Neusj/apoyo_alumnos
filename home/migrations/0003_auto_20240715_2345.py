# Generated by Django 2.2.28 on 2024-07-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20240715_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo',
            field=models.CharField(choices=[('administrador', 'Administrador'), ('docente', 'Docente'), ('apoderado', 'Apoderado'), ('psicologo', 'Psicólogo')], default='alumno', max_length=20),
        ),
    ]
