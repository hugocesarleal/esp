from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ConfiguracaoDispositivo

def index(request):
    # Pega a configuração de ID 1, ou cria se não existir
    config, created = ConfiguracaoDispositivo.objects.get_or_create(id=1)

    if request.method == 'POST':
        novo_numero = request.POST.get('numero')
        if novo_numero and novo_numero.isdigit():
            config.numero = int(novo_numero)
            config.save()
            return redirect('index')

    return render(request, 'core/index.html', {'config': config})

def api_get_numero(request):
    # API simples para o ESP32 fazer o GET
    config, created = ConfiguracaoDispositivo.objects.get_or_create(id=1)
    return JsonResponse({'numero': config.numero})