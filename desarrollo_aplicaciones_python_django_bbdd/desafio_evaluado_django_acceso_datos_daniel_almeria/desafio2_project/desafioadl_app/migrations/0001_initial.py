# Generated by Django 5.0.4 on 2024-04-29 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=150)),
                ('eliminada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=150)),
                ('eliminada', models.BooleanField(default=False)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desafioadl_app.tarea')),
            ],
        ),
    ]
