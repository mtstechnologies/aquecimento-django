from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno

# capturar os dados enviados no formulario e salvar no banco


def criar_aluno(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        # buscando dados do banco para preencher uma tabela no fronend
        alunos = Aluno.objects.all()
        return render(request, 'criar_aluno.html', {'status': status, 'alunos': alunos})
    elif request.method == 'POST':
        # é assim que se pega os dados do formulario para salvar no banco
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')

        # validando os dados do formulario antes de serem salvos
        if len(nome.strip()) == 0:
            return redirect('/aluno/criar_aluno/?status=1')

        if not idade:
            return redirect('/aluno/criar_aluno/?status=2')

        if int(idade) < 0:
            return redirect('/aluno/criar_aluno/?status=3')

        # criando uma instancia da classe modelo, e suas variaveis recebem o que vem do formulario
        aluno = Aluno(
            nome=nome,
            idade=idade,
            email=email
        )
        aluno.save()
        # redirecionando a pagina apos cadastro
        return redirect('criar_aluno')


def listar_aluno(request):
    return HttpResponse('Estou listando os alunos')


def deletar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('criar_aluno')
