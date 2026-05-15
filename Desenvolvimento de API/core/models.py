from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

class Filme(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    sinopse = models.TextField(blank=True)
    ano_lancamento = models.IntegerField()
    nota = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    ingressos = models.IntegerField(default=0)
    preco_ingresso = models.DecimalField(max_digits=10, decimal_places=2)
    genero = models.ForeignKey(Genero,on_delete=models.SET_NULL, null=True, blank=True,related_name='filmes')
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'