from rest_framework import serializers
from .models import Proposta

class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        exclude = ('status',)
