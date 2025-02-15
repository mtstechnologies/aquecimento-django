from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno


def criar_aluno(request):
    if request.method == 'GET':
        return render(request, 'criar_aluno.html')
    elif request.method == 'POST':
        # é assim que se pega os dados do formulario para salvar no banco
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')

        # validando os dados do formulario antes de serem salvos
        '''if len(nome.strip()) == 0 or idade < 0:
            ...'''
    
        # criando uma instancia da classe modelo, e suas variaveis recebem o que vem do formulario
        aluno = Aluno(
            nome=nome,
            idade=idade,
            email=email
        )
        aluno.save()
        #redirecionando a pagina apos cadastro
        return redirect('criar_aluno')


def listar_aluno(request):
    return HttpResponse('Estou listando os alunos')


# capturar os dados enviados no formulario e salvar no banco
