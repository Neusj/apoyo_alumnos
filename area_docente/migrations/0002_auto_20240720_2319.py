# Generated by Django 2.2.28 on 2024-07-21 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area_docente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='segundo_apellido',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
