from rest_framework import viewsets
from app.models import Transacao
from app.api.serializers import TransacaoSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.filter(tipo='R')
    serializer_class = TransacaoSerializer

    def get_queryset(self):
        queryset = self.queryset
        # Aqui você pode adicionar filtros adicionais, como por exemplo, filtrar por data
        return queryset

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.filter(tipo='D')
    serializer_class = TransacaoSerializer
