from rest_framework import viewsets
from .models import Proposta
from .serializers import PropostaCreateSerializer, PropostaRetrieveSerializer

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PropostaCreateSerializer
        return PropostaRetrieveSerializer