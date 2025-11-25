from django.contrib import admin
from main.models import Task_Canil



@admin.register(Task_Canil)
class TaskAdmin(admin.ModelAdmin):
    list_display=('titulo', 'descricao', 'Trabalhos_empregados')
    list_filter = ('concluida','prioridade')
    search_fields = ('titulo',)