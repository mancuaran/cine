# Generated by Django 2.0.3 on 2018-05-17 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cine', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_funcion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('duracion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('asiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.Asiento')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sala', models.CharField(max_length=50)),
                ('cantidad_asientos', models.CharField(max_length=10)),
                ('cine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.Cine')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.Sala'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.Pelicula'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cine.Sala'),
        ),
    ]
