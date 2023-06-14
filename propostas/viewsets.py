from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PropostaCreateSerializer, PropostaRetrieveSerializer
from .models import Proposta
from .tasks import process_proposta

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PropostaCreateSerializer
        return PropostaRetrieveSerializer

    def perform_create(self, serializer):
        proposta = serializer.save()
        process_proposta.delay(proposta.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)