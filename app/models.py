from django.db import models


# Título, Descrição, Categoria, Valor

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Transacao(models.Model):
    TIPO_CHOICES = (
        ('R', 'Receita'),
        ('D', 'Despesa'),
    )
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_ocorrencia = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    pago = models.BooleanField(default=False)  # Para despesas

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Transações"

