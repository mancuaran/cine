from django.shortcuts import render
from django.http import HttpResponse
from cine.models import Pelicula, Funcion, Confiteria
from cine.serializers import FuncionSerializaer
from rest_framework import generics
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.

def pelicula(request):
	pelicula_list = Pelicula.objects.all()
	context = {'object_list': pelicula_list}
	return render(request, 'cine/pelicula.html', context)
	
def lista(request):
	c_list = Confiteria.objects.all()
	context = {'object_list2': c_list}
	return render(request, 'cine/pelicula.html', context)	
	


def pelicula_videos(request):
	pelicula_list = Pelicula.objects.all()
	context = {'object_list': pelicula_list}
	return render(request, 'cine/pelicula_videos.html', context)   



class PeliculaUpdate(UpdateView):
	model = Pelicula
	fields = "__all__"
   
    
class PeliculaCreate(CreateView):
    model = Pelicula
    fields = "__all__"
	

class PeliculaDelete(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('pelicula-list') 

def pelicula_detail(request, pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)
    context = {'object': pelicula}
    return render(request, 'cine/pelicula_detail.html', context)


def funcion(request):
	funcion_list = Funcion.objects.all()
	context = {'object_list': funcion_list}
	return render(request, 'cine/funcion.html', context)

class FuncionUpdate(UpdateView):
	model = Funcion
	fields = "__all__"
   
    
class FuncionCreate(CreateView):
    model = Funcion
    fields = "__all__"
	

class FuncionDelete(DeleteView):
    model = Funcion
    success_url = reverse_lazy('funcion-list') 

class ConfiteriaUpdate(UpdateView):
	model = Confiteria
	fields = "__all__"
   
    
class ConfiteriaCreate(CreateView):
    model = Confiteria
    fields = "__all__"
	

class ConfiteriaDelete(DeleteView):
    model = Confiteria
    success_url = reverse_lazy('confiteria-list')





def confiteria(request):
	confiteria_list = Confiteria.objects.all()
	context = {'object_list': confiteria_list}
	return render(request, 'cine/confiteria.html', context)


def contacto(request):
	confiteria_list = Confiteria.objects.all()
	context = {'object_list': confiteria_list}
	return render(request, 'cine/contacto.html', context)

class funcionDetail(DetailView):
    model = Funcion	

# Serializers

class FuncionList(generics.ListCreateAPIView):
	queryset = Funcion.objects.all()
	serializer_class = FuncionSerializaer

class FuncionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Funcion.objects.all()
	serializer_class = FuncionSerializaer	


	

 


