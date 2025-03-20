from django.db import models


class Book(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank=True)
    data_livro = models.DateField(blank= True, null=True)
    data_cadastro = models.DateField(auto_now_add=True)

    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length = 30, blank=True)
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    tempo_duracao = models.DateField(blank=True, null=True) #contar entre datas.

    def __str__(self):
        return self.nome