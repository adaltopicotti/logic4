from django.db import models

# Create your models here.
class PessoaFisica(models.Model):
    status = models.CharField(max_length=2)
    cpfnumber = models.CharField(max_length=11)
    formattedcpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=200)
    nascimento = models.DateField(blank=True, null=True)
    mae = models.CharField(max_length=200, null=True)
    genero = models.CharField(max_length=2, null=True)
    situacao = models.CharField(max_length=20, null=True)
    consultaID = models.CharField(max_length=50)

    def __str__(self):
        return  self.nome
