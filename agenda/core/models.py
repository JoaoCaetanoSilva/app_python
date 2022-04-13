from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.IntegerField(blank=True, null=True)
    data_titulo = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Tabela'


