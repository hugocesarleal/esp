from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ConfiguracaoDispositivo
import os

def index(request):
    config, created = ConfiguracaoDispositivo.objects.get_or_create(id=1)

    if request.method == 'POST':
        novo_numero = request.POST.get('numero')
        if novo_numero and novo_numero.isdigit():
            config.numero = int(novo_numero)
            config.save()
            return redirect('index')

    return render(request, 'core/index.html', {'config': config})

def api_get_numero(request):
    # Lê a chave esperada da variável de ambiente
    chave_esperada = os.environ.get('ESP32_API_KEY')

    # Lê a chave enviada pelo ESP32 no header
    chave_recebida = request.headers.get('X-API-Key')

    if not chave_esperada or chave_recebida != chave_esperada:
        return JsonResponse({'erro': 'Não autorizado'}, status=401)

    config, created = ConfiguracaoDispositivo.objects.get_or_create(id=1)
    return JsonResponse({'numero': config.numero})