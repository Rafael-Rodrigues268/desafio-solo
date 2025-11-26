from django.shortcuts import render
from main.models import Task_Canil

def task_list(request):
    
    
    tarefas = Task_Canil.objects.all()
    context = {
        'tarefas':tarefas
    }
    return render( request, 'Task/TASK_LIST.html',context)

def task_concluidas(request):
    
    tarefas = Task_Canil.objects.filter(concluida = 1)
    context ={
        'tarefas': tarefas
    }

    return render(request, 'Task/TASK_LIST.html', context)


def task_pendentes(request):
    
    tarefas = Task_Canil.objects.filter(concluida = 0)
    context ={
        'tarefas': tarefas
    }

    return render(request, 'Task/TASK_LIST.html', context)