from django.db import models

class Usuario(models.Model):
    userID = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40)
    telefone = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=40)

    def __str__(self):
        return self.email