from django.db import models


# Create your models here.
class Student(models.Model):
    """
    Classe responsável pelo cadastro de alunos
    """
    name = models.CharField(max_length=50, blank=False)
    idade = models.CharField(max_length=2, blank=False, default="")
    email = models.CharField(max_length=20, blank=False, default="")
    