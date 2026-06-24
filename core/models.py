from django.db import models

class ConfiguracaoDispositivo(models.Model):
    numero = models.IntegerField(default=0)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Número atual: {self.numero}"