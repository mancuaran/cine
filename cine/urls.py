"""myapps2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cine import views
from django.conf.urls import url




urlpatterns = [
    
    path('pelicula',views.pelicula,name='pelicula-list'),
    path('pelicula/videos',views.pelicula_videos,name='pelicula-list'),
    path('pelicula/<int:pelicula_id>/detail/', views.pelicula_detail,
                           name='pelicula-detail'),
    path('pelicula/funcion',views.funcion,name='funcion-list'),
    
    path('pelicula/confiteria',views.confiteria,name='confiteria-list'),
    
    path('pelicula/contacto',views.contacto,name='contacto-list'),
    path('accounts/', include('registration.backends.admin_approval.urls')),
    

    # Update
    path('pelicula/<int:pk>/update/', views.PeliculaUpdate.as_view(), name='pelicula-update'),
    #Create
    path('pelicula/create/', views.PeliculaCreate.as_view(), name='pelicula-create'),
    #Delete
    path('pelicula/<int:pk>/delete/', views.PeliculaDelete.as_view(), name='pelicula-delete'),


    # Update
    path('confiteria/<int:pk>/update/', views.ConfiteriaUpdate.as_view(), name='confiteria-update'),
    #Create
    path('confiteria/create/', views.ConfiteriaCreate.as_view(), name='confiteria-create'),
    #Delete
    path('confiteria/<int:pk>/delete/', views.ConfiteriaDelete.as_view(), name='confiteria-delete'),



    # Update
    path('funcion/<int:pk>/update/', views.FuncionUpdate.as_view(), name='funcion-update'),
    #Create
    path('funcion/create/', views.FuncionCreate.as_view(), name='funcion-create'),
    #Delete
    path('funcion/<int:pk>/delete/', views.FuncionDelete.as_view(), name='funcion-delete'),
    

    #Serializers
    path('api/funcion',views.FuncionList.as_view()),
    path('api/funcion/<int:pk>/detail', views.funcionDetail.as_view()),
    
]
 