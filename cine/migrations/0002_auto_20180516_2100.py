# Generated by Django 2.0.3 on 2018-05-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcion',
            options={'verbose_name': 'Funcion', 'verbose_name_plural': 'Funcion'},
        ),
        migrations.AddField(
            model_name='pelicula',
            name='photo',
            field=models.ImageField(default='SOME STRING', upload_to='photos/'),
        ),
    ]
