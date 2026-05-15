from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Genero, Filme
from .serializers import GeneroSerializer, FilmeSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
 
    
class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    search_fields = ['titulo', 'disponivel']
    ordering_fields = ['preco_ingresso', 'ingresso', 'titulo']
    ordering = ['titulo']
    # def get_queryset(self):
    #     if self.action == 'list':
    #         return Filme.objects.filter(ativa=True).select_related('genero')
    #     return Filme.objects.all().select_related('genero')