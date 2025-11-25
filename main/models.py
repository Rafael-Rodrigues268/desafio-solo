from django.db import models
from django.conf import settings


class Task_Canil(models.Model):

    class Priority(models.TextChoices):
        NIVEL_1 = "1","Pouca performanci"
        NIVEL_2 = "2", "alta performanci"
        NIVEL_3 = "3","performanci Essencial "

    class Area(models.TextChoices):
        Interno = "IN", "Área interna"
        Externa = "EX", "Área externa"
        Canil = "CA", "Área dos cachorros"
        Recepicao = "RE", "Recepição"


    Trabalhos_empregados = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Trabalho",
        null=True,
        blank=True
    )

    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição-afazeres", null=True, blank=True)
    concluida = models.BooleanField("Concluido",default=False)

    prioridade= models.CharField(
        "Prioridades",
        max_length=1,
        choices=Priority.choices,
        default=Priority.NIVEL_1
    )

    data_limite = models.DateField("Data limite", null=True, blank=True)
    mandado_em = models.DateTimeField("mandado em", auto_now_add=True)
    atualizacao_task =models.DateTimeField("tarefa Atualizada", auto_now=True)

    class Meta:
        ordering = ("concluida","data_limite", "-prioridade", "-mandado_em")

        def __str__(self) -> str:
            return self.titulo