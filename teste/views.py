from django.http import HttpResponse
from django.shortcuts import render


def Hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse('O ano passado foi: ' + str(year))


def listaNomes(nome):
    lista_nomes = [
        {'nome': 'Eu', 'idade': 21},
        {'nome': 'Dedeo', 'idade': 17},
        {'nome': 'Gab', 'idade': 21}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}


def fname(request, nome):
    if listaNomes(nome)['nome'] == 'Não encontrado':
        return HttpResponse('Não encontrado')
    else:
        return HttpResponse(
            listaNomes(nome)['nome'] + ' foi encontrada, tem a idade de: ' + str(listaNomes(nome)['idade']))


def pessoas(request, nome):
    nome_lista = listaNomes(nome)['nome']
    idade_lista = listaNomes(nome)['idade']
    return render(request, 'pessoa.html', {'idadeH':idade_lista,'nomeH':nome_lista})
