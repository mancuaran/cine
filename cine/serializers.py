from rest_framework import serializers
from cine.models import  Asiento, Sala, Funcion, Pelicula, Reserva, Confiteria


class FuncionSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Funcion
        fields="__all__"