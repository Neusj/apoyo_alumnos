# Generated by Django 2.2.28 on 2024-07-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]