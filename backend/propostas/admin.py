from django.contrib import admin
from .models import Proposta

class PropostaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'status') 
    list_filter = ('status',)  

admin.site.register(Proposta, PropostaAdmin)
