from django.urls import path
from . import views

urlpatterns = [

path('', views.home, name='home'),

path('cadastrar/', views.cadastrar_livro, name='cadastrar'),
path('confirmacao/', views.confirmacao, name='confirmacao'),

path('consultar/', views.consultar_livro, name='consultar'),
path('resultado/', views.resultado_consulta, name='resultado'),

path('livros/', views.listar_livros, name='lista'),
path('livro/<int:id>/', views.detalhes_livro, name='detalhes'),

path('excluir/<int:id>/', views.excluir_livro, name='excluir'),

path('sobre/', views.sobre, name='sobre'),
path('contato/', views.contato, name='contato'),

]