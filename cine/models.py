from django.db import models

from django.db import models
from django.db.models.signals import post_delete
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver 
from django.urls import reverse








class Asiento(models.Model):
    """ Asiento  """
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return self.puesto

    def get_absolute_url(self):
        return reverse('asiento-list')

class Sala(models.Model):
    """ Sala  """
    
    nombre_sala = models.CharField(max_length=50)
    cantidad_asientos = models.CharField(max_length=10) 

    def __str__(self):
        return self.nombre_sala

    def get_absolute_url(self):
        return reverse('sala-list')
    



class Funcion(models.Model):
    """ Funcion  """
    class Meta:
        verbose_name = _("Funciones")
        verbose_name_plural = _("Funciones")
    

    sala = models.ForeignKey('Sala', on_delete=models.PROTECT )
    fecha_funcion = models.DateTimeField(auto_now=False)
    pelicula = models.ForeignKey('Pelicula', on_delete=models.PROTECT )    



    def __str__(self):
        fu="Funcion:"+" "+str(self.id)
        return fu
        

    def get_absolute_url(self):
        return reverse('funcion-list')

class Pelicula(models.Model):
    """ Cine  """
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/',default='SOME STRING')
    link = models.CharField(max_length=50 ,default='SOME STRING')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('pelicula-list')

@receiver(post_delete, sender=Pelicula)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)



class Confiteria(models.Model): 
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50) 
    photo = models.ImageField(upload_to='photos/',default='SOME STRING')
    precio = models.CharField(max_length=50,default='SOME STRING') 

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('confiteria-list')    

@receiver(post_delete, sender=Confiteria)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)

     


class Reserva(models.Model):
    """ Reserva """
    sala = models.ForeignKey('Sala', on_delete=models.PROTECT )
    asiento = models.ForeignKey('Asiento', on_delete=models.PROTECT  )
    estado = models.BooleanField(default=False)


    def __str__(self):
        re="Reserva:"+" "+str(self.sala)
        return re


    def get_absolute_url(self):
        return reverse('reserva-list')

# Create your models here.
