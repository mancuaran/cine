# Generated by Django 2.0.3 on 2018-05-31 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0002_auto_20180516_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcion',
            options={},
        ),
        migrations.RemoveField(
            model_name='sala',
            name='cine',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='link',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.DeleteModel(
            name='Cine',
        ),
    ]
