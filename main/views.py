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








def task_create(request):

    if request.method == 'POST':
        titulo = request.POST.get('titulo', "").strip()
        descricao = request.POST.get('descricao',"").strip()
        concluida = request.POST.get('concluida', "")== 'on'
        area = request.POST.get('area',"").strip()
        prioridade = request.POST.get('prioridade', "").strip()
        data_limite = request.POST.get('data_limite',"").strip()

        Task_Canil.objects.create(
            titulo=titulo,
            descricao=descricao,
            concluida=concluida,
            area=area,
            prioridade=prioridade,
            data_limite=data_limite
        )

        return redirect ("task_list")

    context ={
        'opcoes_prioridade': Task_Canil.Priority.choices,
    }
    return render(request, 'Task/task_form.html', context)