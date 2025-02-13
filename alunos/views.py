from django.shortcuts import render

from django.http import HttpResponse

def criar_aluno(request):
    return HttpResponse('Ola mundo!')

def listar_aluno(request):
    return HttpResponse('Estou listando os alunos')






