from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import PropostaCreateSerializer, PropostaRetrieveSerializer
from .models import Proposta
from .tasks import processar_proposta
from datetime import datetime, timedelta

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaRetrieveSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return PropostaCreateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        try:
            proposta = serializer.save()
            schedule_time = datetime.now() + timedelta(seconds=5)
            print(f"Enviando proposta {proposta.id}") 
            processar_proposta.apply_async(args=[proposta.id], eta=schedule_time)
        except Proposta.DoesNotExist:
            return Response({"error": "Proposta does not exist."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
