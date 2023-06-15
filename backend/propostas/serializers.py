from rest_framework import serializers
from .models import Proposta

class PropostaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        exclude = ('status',)

class PropostaRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        fields = '__all__'