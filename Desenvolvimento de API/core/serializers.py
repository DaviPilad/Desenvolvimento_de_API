from rest_framework import serializers
from .models import Genero, Filme

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id','nome', 'descricao']

class FilmeSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer(read_only=True)
    Genero_do_Filme = serializers.PrimaryKeyRelatedField(
        queryset=Genero.objects.all(),
        source='genero',
        write_only=True,
        allow_null=True,
        required=False,
    )
    class Meta:
        model = Filme
        fields = [
        'id','titulo', 'sinopse', 'ano_lancamento', 'nota', 'disponivel',
        'criado_em','ingressos', 'preco_ingresso', 'genero','Genero_do_Filme'
    ]
    read_only_fields = ['id', 'criado_em']

    def get_em_estoque(self, ingressos):
        return ingressos.estoque > 0
