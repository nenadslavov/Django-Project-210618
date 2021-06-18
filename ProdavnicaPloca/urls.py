from django.urls import path
from . import views

app_name = 'prodavnicaploca'
urlpatterns = [path('', views.ListaPloca, name='ListaPloca'),
               path('<slug:kategorija_slug>/', views.ListaPloca,
                    name='ListaPlocaPoKategoriji'),
               path('<int:id>/<slug:slug>/', views.DetaljiPloca,
                    name='DetaljiPloca'), ]
