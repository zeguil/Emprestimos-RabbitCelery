from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PropostaCreateSerializer, PropostaRetrieveSerializer
from .models import Proposta
from .tasks import process_proposta

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaRetrieveSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return PropostaCreateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        proposta = serializer.save()
        process_proposta.delay(proposta.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
